# Actual script runs

Inputs use the fictional demonstration business.

## main.py

```text
Welcome to Python for AI!
Run my first task: uv run code/lesson_01_intro.py

```

## code/lesson_01_intro.py

```text
Name: Muhammad Usman Safdar
Dream AI role: AI Agent Developer
Problem I want to solve: Local bakeries spend time answering repeated WhatsApp questions
Why: I want to help small businesses save time with useful AI tools
Muhammad Usman Safdar is building an example AI solution for businesses in Lahore.

```

## code/lesson_04_print_input.py

```text
Your name: Business type: Biggest problem: Monthly budget (PKR, whole number): 
Welcome, Muhammad Usman Safdar!
--- Your AI Prompt ---
Suggest 3 AI solutions for a bakery that struggles with repeated WhatsApp questions. Budget: 15000 PKR per month.

```

## code/lesson_05_variables.py

```text
--- AI Model Profile ---
Model: qwen2.5:3b (<class 'str'>)
Model context capacity: 32768 (<class 'int'>)
Example PKR per 1K tokens: 0.5 (<class 'float'>)
Runs locally: True (<class 'bool'>)
API key: None (<class 'NoneType'>)
Practice pricing only. Local Ollama has no per-token API fee; hardware and electricity still cost money.
Tokens per chat (whole number): Chats per day (whole number): Example cost per chat: 0.5 PKR
Example monthly cost (30 days): 300.0 PKR

```

## code/lesson_06_strings_prompts.py

```text
Your messy question: Your name: Cleaned name: Muhammad Usman Safdar
Cleaned question: How does python work?
Characters: 21
Estimated question tokens: 5
Mentions Python: True
Submitted question characters: 21
Example question-only cost: 0.00 PKR
Practice pricing only; excludes instructions and the answer. Local Ollama has no token API fee.
========================================
You are a friendly Python tutor.
Greet Muhammad Usman Safdar by name and answer in 3 short lines.
Question: How does python work?

```

## code/project_m1_prompt_kit.py

```text
Business name: Business type: City: Main customers: Monthly budget (PKR, whole number): 
============================================================
AI Prompt Kit for Sweet Crumbs
============================================================

[1] Marketing
You are a social media writer for Sweet Crumbs, a bakery in Lahore.
Write one short Instagram post idea for university students and families in a friendly tone, with one call to action.
Do not invent prices, products, opening hours, contact details or discounts; use placeholders if needed.

[2] Customer Service
You are the customer service manager of Sweet Crumbs, a bakery in Lahore serving university students and families.
Write a polite reply of at most 80 words to a customer whose order arrived late.
Apologise and ask them to contact the team privately with their order reference.
Do not invent an explanation or promise a refund or discount without owner approval.

[3] Growth
You are a practical small-business AI adviser for Sweet Crumbs, a bakery in Lahore.
Suggest exactly 3 low-cost AI ideas to attract or serve university students and families within a total monthly budget of 15000 PKR.
Give a concrete first step for each idea. Label any costs as estimates requiring verification.
Do not claim current tool prices or guaranteed results. Include local Ollama with qwen2.5:3b where useful.

[4] WhatsApp Enquiry (bonus)
You are a friendly WhatsApp assistant for Sweet Crumbs, a bakery in Lahore serving university students and families.
Draft an acknowledgement of a new order enquiry in no more than 50 words.
Ask what the customer needs and their preferred date. Use placeholders for unknown details.
Do not claim an order is confirmed or invent availability, prices or delivery times.

```
