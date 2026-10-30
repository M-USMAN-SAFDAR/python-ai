"""A fact-grounded Crumble case-study bot with selectable response personas."""

from langchain.chat_models import init_chat_model

MODEL_NAME = "qwen2.5:3b"
MAX_MESSAGES = 8

# These are illustrative classroom values, not verified Crumble Pakistan business data.
facts = {
    "name": "Crumble Pakistan (student case study)",
    "type": "cookie bakery",
    "city": "Lahore (case-study location)",
    "audience": "university students and families (assumed)",
    "hours": "not supplied; ask the business",
    "delivery": "not supplied; ask the business",
    "prices": {
        "chocolate cookie": 250,
        "double chocolate cookie": 300,
        "cookie box": 1200,
    },
}
personas = {
    "friendly": "Warm and cheerful; use simple words.",
    "formal": "Polite and professional; avoid slang.",
    "sales": "Enthusiastic but honest; suggest at most one relevant item.",
}
config = {"model": MODEL_NAME, "temperature": 0.2, "memory_size": MAX_MESSAGES}


def build_system_message(persona: str) -> str:
    """Ground the assistant in the provided facts and selected tone."""
    return (
        f"You are a {persona} customer assistant for {facts['name']}. "
        f"Business facts: {facts}. Only use these facts. If information is missing, "
        "say you do not know and suggest contacting the business. Never invent prices, "
        "availability, ingredients, hours, or delivery promises. Keep replies short."
    )


llm = init_chat_model(config["model"], model_provider="ollama", temperature=config["temperature"])
messages = [{"role": "system", "content": build_system_message(personas["friendly"])}]
print("Bot ready. Commands: /persona friendly|formal|sales, /price <item>, bye")

while True:
    user_text = input("You: ").strip()
    lower_text = user_text.lower()

    if not user_text:
        print("Bot: Please enter a question.")
    elif lower_text == "bye":
        print("Bot: Goodbye!")
        break
    elif lower_text.startswith("/persona"):
        parts = user_text.split(maxsplit=1)
        requested_persona = parts[1].lower() if len(parts) > 1 else "friendly"
        # .get provides a safe default when a user mistypes a persona.
        selected_persona = personas.get(requested_persona, personas["friendly"])
        messages[0]["content"] = build_system_message(selected_persona)
        print(f"Bot: Style changed to: {selected_persona}")
    elif lower_text.startswith("/price"):
        parts = user_text.split(maxsplit=1)
        item = parts[1].strip().lower() if len(parts) > 1 else ""
        price = facts["prices"].get(item)
        # Prices are answered directly from the dictionary so the model cannot make them up.
        if price is None:
            print(f"Bot: Sorry, {item or 'that item'} is not on our menu.")
        else:
            print(f"Bot: {item.title()} costs {price:,} PKR.")
    else:
        messages.append({"role": "user", "content": user_text})
        messages = [messages[0]] + messages[1:][-config["memory_size"]:]
        response = llm.invoke(messages)
        messages.append({"role": "assistant", "content": response.text})
        messages = [messages[0]] + messages[1:][-config["memory_size"]:]
        print(f"Bot: {response.text}")
