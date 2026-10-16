# Module 1 Project: AI Test Results

**Business:** Crumble Pakistan, cookie bakery, Lahore case-study location.
**Model:** qwen2.5:3b, local Ollama.
**Assumed audience:** university students and families.
**Assumed monthly budget:** 15000 PKR.

[Business facts and assumptions](crumble-business-profile.md) · [Actual script run](project-m1-run.txt)

Independent student testing based on public information, without company involvement. Actual AI answers are preserved verbatim; evaluations were prepared with AI assistance. Temperature: 0.2; context allocation: 4096 tokens. Maximum output: 300 tokens for prompts 1, 2 and 4; 900 for the revised prompt 3. An earlier growth attempt was truncated; it was replaced by this complete retest, whose incorrect advice is evaluated honestly.

## Prompt 1: Marketing

**Prompt:**

```text
You are a social media writer for Crumble Pakistan, a cookie bakery in Lahore.
Write one short Instagram post idea for university students and families in a friendly tone, with one call to action.
Do not invent prices, products, opening hours, contact details or discounts; use placeholders if needed.
```

**AI answer:**

📸 Did you know that baking cookies is not just a fun activity, but also a great way to bond with family and friends? 🍪

At Crumble Pakistan, we're celebrating the joy of baking with our delicious cookie mix. Perfect for those cozy nights in or as a thoughtful gift for your loved ones.

Why not treat yourself and your university students or families to a sweet adventure? 🌟

Let's bake together and create memories that last a lifetime. 🎉

#CrumblePakistan #BakingWithFriends #UniversityMoments #FamilyTime #SweetAdventures

**Useful?** No, needs correction. It invents a cookie-mix product which was neither provided nor verified. It also has several calls to action. Ask for a short cookie post with one call to action and no unverified products.

[Raw response](evidence/crumble-1.json) · generated 2026-10-16T16:54:09.6943774Z · stop reason `stop`.

## Prompt 2: Customer Service

**Prompt:**

```text
You are the customer service manager of Crumble Pakistan, a cookie bakery in Lahore serving university students and families.
Write a polite reply of at most 80 words to a customer whose order arrived late.
Apologise and ask them to contact the team privately with their order reference.
Do not invent an explanation or promise a refund or discount without owner approval.
```

**AI answer:**

Dear Customer, we are sorry to hear that your order arrived late. We would like to assist you privately. Please share your order reference so we can look into this matter. Thank you for your understanding.

**Useful?** Yes, useful as a draft. It apologises, asks for the order reference privately, is under 80 words and avoids an invented reason or promise of compensation. Staff should check it before use.

[Raw response](evidence/crumble-2.json) · generated 2026-10-16T16:54:21.9925496Z · stop reason `stop`.

## Prompt 3: Growth

**Prompt:**

```text
You are a practical small-business AI adviser for Crumble Pakistan, a cookie bakery in Lahore.
Suggest exactly 3 low-cost AI ideas to attract or serve university students and families within a total monthly budget of 15000 PKR.
Keep the advice about Crumble Pakistan's cookie bakery, not a university cafeteria. Use 3 numbered items, at most 45 words each.
Give a concrete first step for each idea. Label any costs as estimates requiring verification.
Do not claim current tool prices or guaranteed results. Include local Ollama with qwen2.5:3b where useful.
```

**AI answer:**

1. **Use ChatGPT for Social Media Engagement**: Create engaging content on Crumble Pakistan's social media profiles. First, verify ChatGPT's capabilities for creating engaging, educational, and promotional content for university students and families.

2. **Implement Ollama for Customized Recommendations**: Use Ollama to generate personalized cookie recommendations based on user preferences. First, set up Ollama and test its accuracy in suggesting cookies that align with university student tastes and dietary restrictions.

3. **Leverage Qwen for Customer Support**: Integrate Qwen for quick and efficient customer support on Crumble Pakistan's website and social media. First, train Qwen on common queries and concerns from university students and families, ensuring quick and accurate responses.

**Useful?** Partly useful for brainstorming. The final retest gives three relevant ideas and first steps without truncation. However, it gives no costs, so it does not establish that setup and monthly operation fit 15000 PKR. Its phrase train Qwen needs clarification: supplying FAQ context is different from training weights. ChatGPT is an additional suggested tool, not evidence of another model tested here. Cookie recommendations involving dietary restrictions need verified product and allergen information and human review. Start with staff-assisted drafts, verify hardware and integration costs, and request a costed PKR plan before implementing.

[Raw response](evidence/crumble-3.json) · generated 2026-10-16T17:03:23.7092791Z · stop reason `stop`.

## Prompt 4: WhatsApp (bonus)

**Prompt:**

```text
You are a friendly WhatsApp assistant for Crumble Pakistan, a cookie bakery in Lahore serving university students and families.
Draft an acknowledgement of a new order enquiry in no more than 50 words.
Ask what the customer needs and their preferred date. Use placeholders for unknown details.
Do not claim an order is confirmed or invent availability, prices or delivery times.
```

**AI answer:**

Hi there! Thanks for reaching out. Could you please let me know what you need and your preferred order date?

**Useful?** Yes, useful as a draft. It thanks the customer and asks what they need and their preferred date without inventing prices or confirming availability. Adding the business name would improve clarity.

[Raw response](evidence/crumble-4.json) · generated 2026-10-16T16:55:28.7620956Z · stop reason `stop`.
