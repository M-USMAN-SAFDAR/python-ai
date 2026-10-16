"""Clean a name and question, then create a short Python tutor prompt."""

raw_question = input("Your messy question: ")
raw_name = input("Your name: ")
# Trimming removes accidental outside spaces; casing follows the lesson exercise.
name = raw_name.strip().title()
question = raw_question.strip().capitalize()
# This simple replacement demonstrates string methods, not a complete word filter.
question = question.replace("stupid", "***").replace("Stupid", "***")
characters = len(question)
# Four English characters per token is a rough estimate, not a tokenizer count.
estimated_tokens = round(characters / 4)
short_question = question[:150]
submitted_tokens = round(len(short_question) / 4)
example_price_per_1k = 0.5
example_cost = submitted_tokens / 1000 * example_price_per_1k

prompt = f"""You are a friendly Python tutor.
Greet {name} by name and answer in 3 short lines.
Question: {short_question}"""

print(f"Cleaned name: {name}")
print(f"Cleaned question: {question}")
print(f"Characters: {characters}")
print(f"Estimated question tokens: {estimated_tokens}")
print(f"Mentions Python: {'python' in question.lower()}")
print(f"Submitted question characters: {len(short_question)}")
print(f"Example question-only cost: {example_cost:.2f} PKR")
print("Practice pricing only; excludes instructions and the answer. Local Ollama has no token API fee.")
print("=" * 40)
print(prompt)
