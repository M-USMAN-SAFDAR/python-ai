"""A hand-built local bakery agent that reads facts, checks orders, and asks before ordering."""

from langchain.chat_models import init_chat_model
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from pydantic import ValidationError

MODEL_NAME = "qwen2.5:3b"
MAX_STEPS = 5
PRICES = {"cupcake": 250, "brownie": 300, "chocolate cake": 1500}
ORDER_STATUS = {"A102": "out for delivery", "A103": "being prepared"}
next_order_number = 104


@tool(parse_docstring=True)
def get_price(item: str) -> str:
    """Read a demo menu price.

    Args:
        item: Menu item to look up.
    """
    price = PRICES.get(item.casefold())
    if price is None:
        return f"{item} is not on the menu."
    return f"{item} costs {price:,} PKR."


@tool(parse_docstring=True)
def order_status(order_id: str) -> str:
    """Check the status of a sample order.

    Args:
        order_id: Order reference supplied by the customer.
    """
    status = ORDER_STATUS.get(order_id.upper())
    if status is None:
        return f"Order {order_id} was not found."
    return f"Order {order_id.upper()} is {status}."


@tool(parse_docstring=True)
def place_order(item: str, quantity: int, customer: str) -> str:
    """Ask the owner for approval before placing a demo order.

    Args:
        item: A menu item to order.
        quantity: Number of units requested.
        customer: Customer's name.
    """
    global next_order_number
    menu_item = next((name for name in PRICES if name.casefold() == item.casefold()), None)
    if menu_item is None:
        return f"Cannot place order: {item} is not on the menu."
    if quantity < 1 or quantity > 20:
        return "Cannot place order: quantity must be from 1 to 20."
    total = PRICES[menu_item] * quantity
    # The approval gate is the only path that can create an order.
    approved = input(
        f"[approve] {quantity} x {menu_item} for {customer} = {total:,} PKR. Place it? (yes/no) "
    ).strip().lower()
    if approved not in {"yes", "y"}:
        return "Order not placed; owner declined or did not approve."
    order_id = f"A{next_order_number}"
    next_order_number += 1
    ORDER_STATUS[order_id] = "received"
    return f"Order {order_id} placed: {quantity} x {menu_item}, total {total:,} PKR"


TOOLS = {tool_.name: tool_ for tool_ in [get_price, order_status, place_order]}
SYSTEM_MESSAGE = (
    "You are a careful bakery assistant. Use tools for menu prices and order status; never guess. "
    "Place an order only when the customer explicitly requests it; the tool will ask the owner "
    "for approval. Do not claim an order was placed unless the tool confirms it."
)
llm = init_chat_model(MODEL_NAME, model_provider="ollama", temperature=0.1).bind_tools(TOOLS.values())
messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
print("Crumble case-study Agent: ask about prices, orders, or place an order. Type 'bye' to exit.")

while True:
    user_text = input("You: ").strip()
    if user_text.lower() == "bye":
        print("Agent: Goodbye!")
        break
    if not user_text:
        print("Agent: Please enter a question.")
        continue

    messages.append({"role": "user", "content": user_text})
    messages = [messages[0]] + messages[1:][-8:]
    order_was_declined = False
    placed_order_result = None
    order_status_result = None
    for step in range(MAX_STEPS):
        response = llm.invoke(messages)
        messages.append(response)
        if not response.tool_calls:
            answer = response.text
            if order_was_declined:
                answer = "The order was not placed because the owner did not approve it."
            elif placed_order_result is not None:
                answer = placed_order_result
            elif order_status_result is not None:
                answer = order_status_result
            print(f"Agent: {answer}")
            break

        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            if tool_name not in TOOLS:
                result = f"Unknown tool: {tool_name}. Choose an available tool."
            else:
                try:
                    result = TOOLS[tool_name].invoke(tool_args)
                    if tool_name == "place_order" and any(
                        word in str(result).casefold()
                        for word in ["not placed", "declined", "cannot place"]
                    ):
                        order_was_declined = True
                    elif tool_name == "place_order" and str(result).startswith("Order A"):
                        placed_order_result = result
                    if tool_name == "order_status":
                        order_status_result = result
                except ValidationError as error:
                    result = f"Invalid tool arguments: {error}"
            print(f"  [tool] {tool_name}({tool_args}) -> {result}")
            messages.append(
                ToolMessage(content=str(result), tool_call_id=tool_call["id"])
            )
    else:
        # The loop bound is a guardrail against a model that keeps requesting tools.
        print("Agent: I could not finish safely in the allowed steps. Please try a simpler request.")
