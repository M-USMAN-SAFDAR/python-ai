# Module 1 Project: AI Test Results

**Business:** Sweet Crumbs, bakery, Lahore — fictional demonstration.
**Audience:** university students and families.
**Monthly budget:** 15000 PKR.
**Model:** qwen2.5:3b, local Ollama.
**Settings:** temperature 0.2, num_ctx 4096, maximum generated tokens 450.

These are actual model responses, preserved verbatim. Reviews were prepared with AI assistance. Testing for a real business is still pending.

## Prompt 1: Marketing

**Prompt:**

```text
You are a social media writer for Sweet Crumbs, a bakery in Lahore.
Write one short Instagram post idea for university students and families in a friendly tone, with one call to action.
Do not invent prices, products, opening hours, contact details or discounts; use placeholders if needed.
```

**AI answer:**

🌟 University Students & Families, Check Out Our Sweet Crumbs Bakes 🌟

Hey there, sweeties! 🎂 If you're a university student or a family on the go, we've got a treat for you. 🏃‍♂️💨

We're launching a special "University & Family Day" where we're offering a delightful treat just for you. 🎁

Come by and grab a sweet from our bakery. It's perfect for those mid-semester breaks or anytime you need a little sweetness in your life. 🌟

Don't forget to tag us and share your treats with us! 📸 #SweetCrumbs #UniversityBakery #FamilyDay

Where are you heading next? 🏠🎓 #UniversityLife #FamilyTime

Happy baking and snacking! 🍰✨

**Useful?** Needs revision. It invents a "University & Family Day" event despite the instruction not to invent details. It is long for a short post and includes several calls to action. Do not publish it as factual business content. Keep the bakery name and audience, remove the invented event, and ask for one short post with one call to action.

**Evidence:** [Raw response](evidence/project-1.json); generated 2026-10-16T16:32:15.1464214Z; stop reason `stop`.

## Prompt 2: Customer Service

**Prompt:**

```text
You are the customer service manager of Sweet Crumbs, a bakery in Lahore serving university students and families.
Write a polite reply of at most 80 words to a customer whose order arrived late.
Apologise and ask them to contact the team privately with their order reference.
Do not invent an explanation or promise a refund or discount without owner approval.
```

**AI answer:**

Dear Customer, 

We apologize for the delay in your order. Our team is working on it now. Please contact us privately with your order reference for any further assistance. 

Thank you for your understanding.

**Useful?** Partly useful. It is polite, brief, apologises, requests the order reference privately, and avoids promising compensation. However, "Our team is working on it now" asserts an unverified operational fact. Replace that with "Please send your order reference privately so we can check what happened."

**Evidence:** [Raw response](evidence/project-2.json); generated 2026-10-16T16:32:25.150402Z; stop reason `stop`.

## Prompt 3: Growth

**Prompt:**

```text
You are a practical small-business AI adviser for Sweet Crumbs, a bakery in Lahore.
Suggest exactly 3 low-cost AI ideas to attract or serve university students and families within a total monthly budget of 15000 PKR.
Give a concrete first step for each idea. Label any costs as estimates requiring verification.
Do not claim current tool prices or guaranteed results. Include local Ollama with qwen2.5:3b where useful.
```

**AI answer:**

Certainly! Here are three low-cost AI ideas to attract or serve university students and families within a total monthly budget of 15000 PKR. I'll provide a concrete first step for each idea, along with a rough estimate for verification.

### 1. **AI-Powered Recipe Recommendation System**
**Objective:** Offer personalized recipe recommendations based on user preferences and dietary needs.

**First Step:** 
- **Create a basic user profile:** Develop a simple web form or mobile app that collects basic information such as dietary preferences (vegan, gluten-free, etc.), favorite cuisines, and any allergies. This can be done using a local Ollama with qwen2.5:3b for initial setup and testing.

**Estimate:** 1000 PKR for basic form development and setup.

### 2. **AI Chatbot for University Students**
**Objective:** Provide quick and personalized assistance to university students and their families.

**First Step:** 
- **Set up a basic chatbot:** Use a local Ollama with qwen2.5:3b to create a simple chatbot that can answer common questions about ordering, delivery, and special offers. Train the chatbot with a few common queries and responses.

**Estimate:** 500 PKR for chatbot setup and initial training.

### 3. **AI-Generated Social Media Content**
**Objective:** Increase brand visibility and engagement through AI-generated social media posts.

**First Step:** 
- **Develop a content calendar:** Use a local Ollama with qwen2.5:3b to generate a content calendar for social media posts. The AI can suggest recipes, promotions, and educational content related to baking and nutrition. This will help in planning and scheduling posts.

**Estimate:** 2000 PKR for content calendar generation and initial content creation.

### Summary:
- **AI-Powered Recipe Recommendation System:** 1000 PKR
- **AI Chatbot for University Students:** 500 PKR
- **AI-Generated Social Media Content:** 2000 PKR

**Total Estimate:** 3500 PKR

These ideas

**Useful?** Useful as brainstorming only. It proposes three ideas and first steps, and the stated estimates sum to 3500 PKR, below the example budget. Those numbers are unverified inventions, not vendor quotes, and do not cover hardware, electricity or maintenance. The answer ends mid-sentence because the generation reached the 450-token cap. A recipe tool also needs careful handling of allergy information and is less relevant than basic order FAQs. A few example questions provide prompt context; they do not train model weights. Prefer the content-calendar idea, verify costs and business facts, and request a shorter revised answer before client use.

**Evidence:** [Raw response](evidence/project-3.json); generated 2026-10-16T16:34:04.7117898Z; stop reason `length`.

## Prompt 4: WhatsApp (bonus)

**Prompt:**

```text
You are a friendly WhatsApp assistant for Sweet Crumbs, a bakery in Lahore serving university students and families.
Draft an acknowledgement of a new order enquiry in no more than 50 words.
Ask what the customer needs and their preferred date. Use placeholders for unknown details.
Do not claim an order is confirmed or invent availability, prices or delivery times.
```

**AI answer:**

Hi Sweet Crumbs! Thanks for your order enquiry. What would you like to order and on what date?

**Useful?** Needs a small correction. It asks for the item and date and avoids invented prices or order confirmation, but greets the bakery ("Hi Sweet Crumbs!") instead of its customer. Replace the opening with "Hi! Thanks for contacting Sweet Crumbs."

**Evidence:** [Raw response](evidence/project-4.json); generated 2026-10-16T16:34:12.9802005Z; stop reason `stop`.
