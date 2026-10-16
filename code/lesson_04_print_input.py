"""Build a business prompt that can be pasted into a local AI model."""

# Personal details make the greeting relevant to the person using the tool.
name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")
# Convert the budget because input returns text rather than a number.
budget = int(input("Monthly budget (PKR, whole number): "))

# A specific problem and spending limit help the AI suggest practical options.
prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}. Budget: {budget} PKR per month."
print(f"\nWelcome, {name}!")
print("--- Your AI Prompt ---")
print(prompt)
