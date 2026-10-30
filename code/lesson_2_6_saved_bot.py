"""A local FAQ bot that saves chat history and reports connection or model errors."""

import json
from pathlib import Path

import httpx
import ollama
from langchain.chat_models import init_chat_model

MODEL_NAME = "qwen2.5:3b"
FAQ_PATH = Path("faq.json")
HISTORY_PATH = Path("chat_history.json")
ERROR_PATH = Path("errors.log")


def log_error(message: str) -> None:
    """Append a technical error for the project owner to inspect."""
    with ERROR_PATH.open("a", encoding="utf-8") as error_file:
        error_file.write(message + "\n")


def save_history(history: list[dict[str, str]]) -> None:
    """Save only plain role/content dictionaries as readable UTF-8 JSON."""
    with HISTORY_PATH.open("w", encoding="utf-8") as history_file:
        json.dump(history, history_file, indent=2, ensure_ascii=False)


if not FAQ_PATH.exists():
    print("Business facts file faq.json is missing. Create it in the code folder first.")
    raise SystemExit(1)

try:
    with FAQ_PATH.open(encoding="utf-8") as faq_file:
        facts = json.load(faq_file)
except (json.JSONDecodeError, OSError) as error:
    print(f"Could not read faq.json: {error}")
    raise SystemExit(1)

system_message = {
    "role": "system",
    "content": (
        f"You are a concise customer assistant. Business facts: {facts}. "
        "Only use these facts. Admit when information is missing; never invent prices, hours, "
        "delivery promises, ingredients, or policies."
    ),
}

if HISTORY_PATH.exists():
    try:
        with HISTORY_PATH.open(encoding="utf-8") as history_file:
            old_history = json.load(history_file)
        if not isinstance(old_history, list) or any(
            not isinstance(message, dict)
            or message.get("role") not in {"user", "assistant"}
            or not isinstance(message.get("content"), str)
            for message in old_history
        ):
            raise ValueError("history must be a list of role/content dictionaries")
        history = [system_message] + old_history[-8:]
        print(f"Loaded {len(history) - 1} old messages.")
    except (json.JSONDecodeError, OSError, ValueError):
        # Damaged persistence should not prevent a fresh conversation.
        print("History file was damaged. Starting a fresh chat.")
        log_error("Damaged chat_history.json; started a fresh chat.")
        history = [system_message]
else:
    history = [system_message]

llm = init_chat_model(MODEL_NAME, model_provider="ollama", temperature=0.2)
print("Crumble case-study Bot: Ask me anything. Commands: /reset, bye")
while True:
    user_text = input("You: ").strip()
    if not user_text:
        print("Bot: Please type a message.")
        continue
    if user_text.lower() == "bye":
        save_history(history[1:])
        print("Bot: Goodbye! Your chat is saved.")
        break
    if user_text.lower() == "/reset":
        history = [system_message]
        save_history([])
        print("Bot: Memory cleared.")
        continue

    history.append({"role": "user", "content": user_text})
    history = [history[0]] + history[1:][-8:]
    try:
        response = llm.invoke(history)
    except (httpx.ConnectError, ollama.ResponseError) as error:
        # Remove an unanswered message so a future session does not treat it as answered.
        history.pop()
        log_error(f"{type(error).__name__}: {error}")
        save_history(history[1:])
        print("Bot: I am offline or the model had a problem. Please try again later.")
        continue

    history.append({"role": "assistant", "content": response.text})
    # Save after each successful turn so a restart can recover the conversation.
    save_history(history[1:])
    print(f"Bot: {response.text}")
