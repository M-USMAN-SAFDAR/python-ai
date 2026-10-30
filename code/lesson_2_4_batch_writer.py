"""Generate short menu descriptions from illustrative bakery product data."""

from langchain.chat_models import init_chat_model

MODEL_NAME = "qwen2.5:3b"
# Demo prices only: no current Crumble Pakistan prices were provided or verified.
products = {
    "Chocolate cookie": 250,
    "Double chocolate cookie": 300,
    "Cookie box": 1200,
    "Gift box": 1800,
    "Seasonal cookie": 0,
}

# Create one model connection and reuse it for every product.
creative = init_chat_model(MODEL_NAME, model_provider="ollama", temperature=0.8)
descriptions = []
total_tokens = 0
total_seconds = 0.0

for product_name, price in products.items():
    if price == 0:
        # Do not ask the AI to promote an item that is not available yet.
        print(f"Skipping {product_name} (coming soon)")
        continue
    response = creative.invoke(
        f"Write one appealing, truthful sentence describing a {product_name} "
        "for a cookie bakery. Do not invent ingredients or product features."
    )
    descriptions.append({"item": product_name, "price": price, "text": response.text})
    total_tokens += response.usage_metadata["total_tokens"]
    total_seconds += response.response_metadata["total_duration"] / 1_000_000_000

print("=" * 50)
for number, item in enumerate(descriptions, start=1):
    print(f"{number}. {item['item']} ({item['price']:,} PKR)")
    print(f"   {item['text']}")
print("=" * 50)
print(f"{len(descriptions)} descriptions, {total_tokens:,} tokens, {total_seconds:.1f} seconds")
