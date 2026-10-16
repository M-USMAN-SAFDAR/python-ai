# Module 1 Project: Crumble Pakistan AI Test Results

**Business:** Crumble Pakistan, cookie bakery; Lahore case-study location.
**Assumed campaign audience:** university students and families.
**Assumed monthly budget:** 15000 PKR.
**Model:** qwen2.5:3b, local Ollama; temperature 0.2, num_ctx 4096, num_predict 300.

See [verified sources and assumptions](crumble-business-profile.md) and [actual script run](crumble-run.txt). This is independent student testing using public information, not a commissioned engagement or company-approved output. Reviews were prepared with AI assistance.

## Prompt 1: Marketing

**Prompt:**

```text
You are a social media writer for Crumble Pakistan, a cookie bakery in Lahore.
Write one short Instagram post idea for university students and families in a friendly tone, with one call to action.
Do not invent prices, products, opening hours, contact details or discounts; use placeholders if needed.
```

**Actual AI answer:**

📸 Did you know that baking cookies is not just a fun activity, but also a great way to bond with family and friends? 🍪

At Crumble Pakistan, we're celebrating the joy of baking with our delicious cookie mix. Perfect for those cozy nights in or as a thoughtful gift for your loved ones. 

Why not treat yourself and your university students or families to a sweet adventure? 🌟

Let's bake together and create memories that last a lifetime. 🎉

#CrumblePakistan #BakingWithFriends #UniversityMoments #FamilyTime #SweetAdventures

**Useful?** Not ready to use. The answer invents a Crumble cookie-mix product which was not supplied in the prompt or verified in the sources. It also includes several calls to action instead of one. Keep the friendly tone, remove the unverified product claim, and request a shorter revised draft about cookies.

**Raw evidence:** [crumble-1.json](evidence/crumble-1.json). Generated 2026-10-16T16:54:09.6943774Z; stop reason `stop`.

## Prompt 2: Customer Service

**Prompt:**

```text
You are the customer service manager of Crumble Pakistan, a cookie bakery in Lahore serving university students and families.
Write a polite reply of at most 80 words to a customer whose order arrived late.
Apologise and ask them to contact the team privately with their order reference.
Do not invent an explanation or promise a refund or discount without owner approval.
```

**Actual AI answer:**

Dear Customer, we are sorry to hear that your order arrived late. We would like to assist you privately. Please share your order reference so we can look into this matter. Thank you for your understanding.

**Useful?** Useful as a draft for the hypothetical complaint. It apologises, asks for an order reference privately and stays under 80 words. It does not invent a reason or promise compensation. A real employee must verify the complaint and approve the wording before sending.

**Raw evidence:** [crumble-2.json](evidence/crumble-2.json). Generated 2026-10-16T16:54:21.9925496Z; stop reason `stop`.

## Prompt 3: Growth

**Prompt:**

```text
You are a practical small-business AI adviser for Crumble Pakistan, a cookie bakery in Lahore.
Suggest exactly 3 low-cost AI ideas to attract or serve university students and families within a total monthly budget of 15000 PKR.
Give a concrete first step for each idea. Label any costs as estimates requiring verification.
Do not claim current tool prices or guaranteed results. Include local Ollama with qwen2.5:3b where useful.
```

**Actual AI answer:**

Certainly! Here are three low-cost AI ideas to attract or serve university students and families within a total monthly budget of 15,000 PKR, along with a concrete first step for each idea:

### 1. **AI-Powered Online Ordering System for University Cafeterias**
**Objective:** Increase sales and convenience for university students by offering a seamless online ordering system.

**First Step:** 
- **Verification:** Research and verify the cost of integrating an AI-powered online ordering system with a university cafeteria. This could include costs for software development, integration, and possibly a monthly subscription fee.
- **Implementation:** Work with the university cafeteria management to set up an online ordering system. This could involve setting up a website or mobile app for ordering, and possibly integrating with payment gateways.

**Estimated Cost:** 5000 PKR (This is an estimate and will need to be verified based on the specific system chosen.)

### 2. **AI-Powered Chatbot for University Cafeteria Information**
**Objective:** Provide quick and accurate information to university students and families about cafeteria hours, menu options, and special offers.

**First Step:** 
- **Verification:** Research and verify the cost of developing an AI-powered chatbot for the university cafeteria. This could include costs for AI development, training, and possibly a monthly maintenance fee.
- **Implementation:** Work with the cafeteria management to train the AI chatbot on relevant information and integrate it into the cafeteria’s existing communication

**Useful?** Not ready to use. The output shifts from the cookie bakery to university cafeterias and does not deliver all three ideas. Generation stopped at the 300-token limit, with stop reason length. Its 5000 PKR figure is an unverified estimate; it does not establish that the entire plan fits the budget. Ask for a shorter response of three numbered items about the bakery, with realistic verification steps. This raw answer is retained as evidence of a failed generation, not a completed business plan.

**Raw evidence:** [crumble-3.json](evidence/crumble-3.json). Generated 2026-10-16T16:55:21.3945532Z; stop reason `length`.

## Prompt 4: WhatsApp (bonus)

**Prompt:**

```text
You are a friendly WhatsApp assistant for Crumble Pakistan, a cookie bakery in Lahore serving university students and families.
Draft an acknowledgement of a new order enquiry in no more than 50 words.
Ask what the customer needs and their preferred date. Use placeholders for unknown details.
Do not claim an order is confirmed or invent availability, prices or delivery times.
```

**Actual AI answer:**

Hi there! Thanks for reaching out. Could you please let me know what you need and your preferred order date?

**Useful?** Useful as a short draft. It thanks the customer and asks what they need and their preferred date without inventing prices, availability or confirmation. It omits the business name, so staff could add Crumble Pakistan for clarity. Staff should approve the draft before using it.

**Raw evidence:** [crumble-4.json](evidence/crumble-4.json). Generated 2026-10-16T16:55:28.7620956Z; stop reason `stop`.

