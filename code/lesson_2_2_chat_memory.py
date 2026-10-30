"""A local AI tutor that remembers a bounded conversation until reset."""

from langchain.chat_models import init_chat_model

MODEL_NAME = "qwen2.5:3b"
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are a friendly Python tutor. Answer clearly in 2 short paragraphs.",
}
MAX_MESSAGES = 8

# Keeping the system message separate means reset and trimming cannot remove the rules.
messages = [SYSTEM_MESSAGE]
llm = init_chat_model(MODEL_NAME, model_provider="ollama", temperature=0.2)

print("Tutor: Ask me anything. Commands: /reset, /count, bye")
while True:
    user_text = input("You: ").strip()

    if not user_text:
        print("Tutor: Please type a question.")
        continue
    if user_text.lower() == "bye":
        print("Tutor: Goodbye!")
        break
    if user_text.lower() == "/reset":
        messages = [SYSTEM_MESSAGE]
        print("Tutor: Memory cleared.")
        continue
    if user_text.lower() == "/count":
        print(f"Tutor: {len(messages)} messages in memory.")
        continue

    messages.append({"role": "user", "content": user_text})
    # System rules plus a bounded tail keep each prompt useful without growing forever.
    messages = [messages[0]] + messages[1:][-MAX_MESSAGES:]
    response = llm.invoke(messages)
    messages.append({"role": "assistant", "content": response.text})
    messages = [messages[0]] + messages[1:][-MAX_MESSAGES:]
    print(f"Tutor: {response.text}")
    print(f"       (tokens sent: {response.usage_metadata['input_tokens']:,})")
