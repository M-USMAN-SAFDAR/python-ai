"""Ask a local AI tutor to explain a topic at the learner's chosen level."""

from langchain.chat_models import init_chat_model

topic = input("Topic: ").strip()
level = input("Level (beginner or expert): ").strip()

# Keeping the role and length in one system message makes each request predictable.
system_message = f"""You are a patient Python tutor.
Explain {topic} for a {level} learner in 3 short sentences.
Use a small code example when it helps."""

# A low temperature is useful here because the tutor should explain clearly and consistently.
llm = init_chat_model("qwen2.5:3b", model_provider="ollama", temperature=0.2)
response = llm.invoke(
    [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"Explain {topic}."},
    ]
)

seconds = response.response_metadata["total_duration"] / 1_000_000_000
total_tokens = response.usage_metadata["total_tokens"]

print("=" * 40)
print(response.text)
print("=" * 40)
print(f"{total_tokens:,} tokens in {seconds:.1f} seconds")
