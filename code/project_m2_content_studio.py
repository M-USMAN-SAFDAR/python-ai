"""Generate and answer customer content requests for a Crumble bakery case study."""

from time import perf_counter

from langchain.chat_models import init_chat_model

config = {"model": "qwen2.5:3b", "max_messages": 8, "cloud_price_per_1k": 0.50}
# All prices and service details here are classroom demo assumptions, not company facts.
facts = {
    "name": "Crumble Pakistan (student case study)",
    "type": "cookie bakery",
    "city": "Lahore (case-study location)",
    "audience": "university students and families (assumed)",
    "hours": "not supplied; confirm with the business",
    "delivery": "not supplied; confirm with the business",
    "prices": {
        "Chocolate cookie": 250,
        "Double chocolate cookie": 300,
        "Cookie box": 1200,
        "Gift box": 1800,
        "Seasonal cookie": 0,
    },
}
tones = {
    "fun": "playful, cheerful, and brief",
    "premium": "elegant and calm, focused on craftsmanship without claiming unverified features",
    "urgent": "energetic but not pushy; do not invent deadlines or scarcity",
}

# Separate settings support careful customer answers and more imaginative marketing.
precise = init_chat_model(config["model"], model_provider="ollama", temperature=0.2)
creative = init_chat_model(config["model"], model_provider="ollama", temperature=0.8, stream_usage=True)
facts_text = "; ".join(f"{key}: {value}" for key, value in facts.items())
SYSTEM_MESSAGE = (
    f"You are the careful customer assistant for {facts['name']}. Business facts: {facts_text}. "
    "Only use these facts. If you do not know, say so. Never invent prices, hours, ingredients, "
    "availability, discounts, or delivery promises. A price of 0 means coming soon and is not free."
)
CREATIVE_SYSTEM = (
    f"You write short draft copy for {facts['name']}, a {facts['type']} in {facts['city']}. "
    "The only supplied product facts are the exact product names and demo prices in the menu. "
    "A price of 0 means coming soon and is not free. "
    "Do not change the business type or invent ingredients, flavors, texture, sourcing, location "
    "details, opening hours, offers, or product descriptions. If a claim is not supplied, omit it. "
    "Return a brief draft that a person will verify before publishing."
)
messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
counts = {"chat_answers": 0, "menu_descriptions": 0, "posts": 0, "price_answers": 0}
total_tokens = 0
total_seconds = 0.0

print("=" * 50)
print(f"   {facts['name']} AI Content Studio")
print("=" * 50)
print("Commands: /menu, /post fun|premium|urgent, /price <item>, /reset, bye")

while True:
    command = input("You: ").strip()
    lower_command = command.lower()

    if not command:
        print("Studio: Please enter a command or question.")
    elif lower_command == "bye":
        print("Studio: Goodbye!")
        break
    elif lower_command == "/reset":
        messages = [messages[0]]
        print("Studio: Chat memory cleared.")
    elif lower_command == "/menu":
        menu = []
        for item_name, item_price in facts["prices"].items():
            if item_price == 0:
                # Skipping unavailable items avoids an unnecessary AI call and invented product copy.
                print(f"Studio: Skipping {item_name} (coming soon)")
                continue
            start = perf_counter()
            response = creative.invoke(
                [
                    {"role": "system", "content": CREATIVE_SYSTEM},
                    {
                        "role": "user",
                        "content": f"Write one neutral sentence using only this product name: {item_name}.",
                    },
                ]
            )
            total_seconds += perf_counter() - start
            total_tokens += response.usage_metadata["total_tokens"]
            menu.append({"item": item_name, "price": item_price, "text": response.text})
            counts["menu_descriptions"] += 1
        print("-" * 50)
        print("AI draft: verify product claims before publishing.")
        for number, item in enumerate(menu, start=1):
            print(f"{number}. {item['item']} ({item['price']:,} PKR)")
            print(f"   {item['text']}")
        print("-" * 50)
    elif lower_command.startswith("/post"):
        parts = command.split(maxsplit=1)
        requested_tone = parts[1].lower() if len(parts) > 1 else "fun"
        # The fallback ensures a typo still produces a post in a safe default style.
        tone_description = tones.get(requested_tone, tones["fun"])
        prompt = (
            f"Write exactly 2 short sentences about the listed cookie products for {facts['name']}. "
            f"Tone: {tone_description}. Only use the facts in the system message. Do not invent "
            "a business type, product, ingredient, offer, location detail, or claim."
        )
        print(f"Studio ({tone_description}; AI draft—verify before publishing):")
        start = perf_counter()
        for chunk in creative.stream(
            [
                {"role": "system", "content": CREATIVE_SYSTEM},
                {"role": "user", "content": prompt},
            ]
        ):
            print(chunk.text, end="", flush=True)
            if chunk.usage_metadata:
                total_tokens += chunk.usage_metadata.get("total_tokens", 0)
        print()
        total_seconds += perf_counter() - start
        counts["posts"] += 1
    elif lower_command.startswith("/price"):
        parts = command.split(maxsplit=1)
        requested_item = parts[1].strip().casefold() if len(parts) > 1 else ""
        # Normalize the lookup, but use the dictionary's exact display name for output.
        menu_key = next(
            (name for name in facts["prices"] if name.casefold() == requested_item), None
        )
        counts["price_answers"] += 1
        if menu_key is None:
            print("Studio: That item is not on our menu.")
        elif facts["prices"][menu_key] == 0:
            print(f"Studio: {menu_key} is coming soon.")
        else:
            print(f"Studio: {menu_key} costs {facts['prices'][menu_key]:,} PKR.")
    else:
        messages.append({"role": "user", "content": command})
        # Keep the system message plus only the latest exchanges so prompt cost stays bounded.
        messages = [messages[0]] + messages[1:][-config["max_messages"]:]
        start = perf_counter()
        response = precise.invoke(messages)
        total_seconds += perf_counter() - start
        total_tokens += response.usage_metadata["total_tokens"]
        messages.append({"role": "assistant", "content": response.text})
        messages = [messages[0]] + messages[1:][-config["max_messages"]:]
        counts["chat_answers"] += 1
        print(f"Studio: {response.text}")
        print(f"        (memory: {len(messages) - 1} messages, {response.usage_metadata['input_tokens']:,} tokens sent)")

print("=" * 50)
print("Session report")
print(f"Chat answers: {counts['chat_answers']} | Menu descriptions: {counts['menu_descriptions']} | Posts: {counts['posts']} | Price answers: {counts['price_answers']}")
print(f"AI usage: {total_tokens:,} tokens in {total_seconds:.1f} seconds")
print("=" * 50)
