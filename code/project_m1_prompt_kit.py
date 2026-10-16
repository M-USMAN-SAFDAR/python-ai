"""Help a local business owner create AI prompts for everyday business tasks."""

# Business details make the prompts useful to one owner instead of generic.
business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
customers = input("Main customers: ")
# Convert the budget to a whole number so later lessons can calculate spending.
budget = int(input("Monthly budget (PKR, whole number): "))

# Roles, audiences and output limits give the model clear instructions.
marketing_prompt = f"""You are a social media writer for {business_name}, a {business_type} in {city}.
Write one short Instagram post idea for {customers} in a friendly tone, with one call to action.
Do not invent prices, products, opening hours, contact details or discounts; use placeholders if needed."""
service_prompt = f"""You are the customer service manager of {business_name}, a {business_type} in {city} serving {customers}.
Write a polite reply of at most 80 words to a customer whose order arrived late.
Apologise and ask them to contact the team privately with their order reference.
Do not invent an explanation or promise a refund or discount without owner approval."""
growth_prompt = f"""You are a practical small-business AI adviser for {business_name}, a {business_type} in {city}.
Suggest exactly 3 low-cost AI ideas to attract or serve {customers} within a total monthly budget of {budget} PKR.
Keep the advice about {business_name}'s {business_type}, not a university cafeteria. Use 3 numbered items, at most 45 words each.
Give a concrete first step for each idea. Label any costs as estimates requiring verification.
Do not claim current tool prices or guaranteed results. Include local Ollama with qwen2.5:3b where useful."""
# A WhatsApp draft is a useful extra task, but the owner must check all details.
whatsapp_prompt = f"""You are a friendly WhatsApp assistant for {business_name}, a {business_type} in {city} serving {customers}.
Draft an acknowledgement of a new order enquiry in no more than 50 words.
Ask what the customer needs and their preferred date. Use placeholders for unknown details.
Do not claim an order is confirmed or invent availability, prices or delivery times."""

print("\n" + "=" * 60)
print(f"AI Prompt Kit for {business_name}")
print("=" * 60)
print(f"\n[1] Marketing\n{marketing_prompt}")
print(f"\n[2] Customer Service\n{service_prompt}")
print(f"\n[3] Growth\n{growth_prompt}")
print(f"\n[4] WhatsApp Enquiry (bonus)\n{whatsapp_prompt}")
