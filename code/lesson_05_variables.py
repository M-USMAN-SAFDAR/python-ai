"""Display a local Qwen model profile and practise token cost calculations."""

model_name = "qwen2.5:3b"
# The 3B model card specifies 32,768 tokens; actual Ollama settings can be lower.
context_window = 32768
# This invented price is for arithmetic practice, not an Ollama charge.
price_per_1k_tokens = 0.5
runs_locally = True
api_key = None

print("--- AI Model Profile ---")
print(f"Model: {model_name} ({type(model_name)})")
print(f"Model context capacity: {context_window} ({type(context_window)})")
print(f"Example PKR per 1K tokens: {price_per_1k_tokens} ({type(price_per_1k_tokens)})")
print(f"Runs locally: {runs_locally} ({type(runs_locally)})")
print(f"API key: {api_key} ({type(api_key)})")
print("Practice pricing only. Local Ollama has no per-token API fee; hardware and electricity still cost money.")

# Numeric conversion allows multiplication instead of repeating input text.
tokens_used = int(input("Tokens per chat (whole number): "))
chats_per_day = int(input("Chats per day (whole number): "))
chat_cost = tokens_used / 1000 * price_per_1k_tokens
monthly_cost = chat_cost * chats_per_day * 30
print(f"Example cost per chat: {round(chat_cost, 2)} PKR")
print(f"Example monthly cost (30 days): {round(monthly_cost, 2)} PKR")
