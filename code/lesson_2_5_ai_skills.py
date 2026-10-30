"""Reusable AI writing skills for a small bakery's daily customer work."""

import sys

from langchain.chat_models import init_chat_model

# Urdu translation output must be printable in the default Windows terminal code page.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MODEL_NAME = "qwen2.5:3b"
# These are student exercise settings, not verified company facts or current prices.
precise = init_chat_model(MODEL_NAME, model_provider="ollama", temperature=0.2)
creative = init_chat_model(MODEL_NAME, model_provider="ollama", temperature=0.8)


def ask_ai(prompt: str, system: str = "You are a helpful bakery assistant.", creative_mode: bool = False) -> str:
    """Send one prompt to the selected model and return its text."""
    model = creative if creative_mode else precise
    response = model.invoke(
        [{"role": "system", "content": system}, {"role": "user", "content": prompt}]
    )
    return response.text


def summarize_text(text: str) -> str:
    """Summarize a bakery message in one short sentence."""
    return ask_ai(f"Summarize this message in one sentence:\n{text}")


def translate_text(text: str, language: str = "Urdu") -> str:
    """Translate customer text into the requested language."""
    return ask_ai(
        f"Translate this text to {language}. Return only the translation:\n{text}",
        system="You are a careful translator. Preserve meaning and do not add details.",
    )


def reply_to_review(review: str) -> str:
    """Draft a polite response to a customer review without making promises."""
    return ask_ai(
        f"Write a short, kind reply to this review. Do not promise compensation:\n{review}",
        creative_mode=True,
    )


def estimate_tokens(text: str) -> int:
    """Estimate English words as a rough token count for a review."""
    return len(text.split())


# These deterministic checks make sure the small local utility works without an AI call.
assert estimate_tokens("four word review here") == 4
assert estimate_tokens("") == 0

skills = {"/summarize": summarize_text, "/translate": translate_text, "/reply": reply_to_review}
usage = {"summarize": 0, "translate": 0, "reply": 0}
print("Crumble case-study AI Toolkit. Commands: /summarize, /translate, /reply, bye")

while True:
    command = input("Command: ").strip().lower()
    if command == "bye":
        break
    skill = skills.get(command)
    if skill is None:
        print("Unknown command. Try /summarize, /translate, /reply or bye.")
        continue

    if command == "/summarize":
        text = input("Text to summarize: ").strip()
        answer = summarize_text(text)
        usage["summarize"] += 1
    elif command == "/translate":
        text = input("Text to translate: ").strip()
        language = input("Language (Enter for Urdu): ").strip() or "Urdu"
        answer = translate_text(text, language)
        usage["translate"] += 1
    else:
        text = input("Customer review: ").strip()
        answer = reply_to_review(text)
        usage["reply"] += 1

    print(f"AI: {answer}")
    if command == "/reply":
        print(f"    (review was about {estimate_tokens(text)} words)")

print("Skills used today:")
for skill_name, skill_count in usage.items():
    print(f"  {skill_name}: {skill_count}")
