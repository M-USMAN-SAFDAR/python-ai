# Module 2 Checkpoint 1: AI Quality Results

Live runs used local Ollama `qwen2.5:3b`. Prices and product details were demo assumptions; none were supplied or verified by the business.

| Test | Question/prompt | Actual answer | Evaluation |
|---|---|---|---|
| Known fact | `What type of business is Crumble Pakistan?` | `Crumble Pakistan is a cookie bakery.` | Correct for the supplied fact. |
| Price | `/price COOKIE BOX` | `Cookie box costs 1,200 PKR.` | Correct deterministic dictionary answer; no AI call. |
| Unknown fact | `Do you sell pizza?` | `No, based on the provided information, Crumble Pakistan does not sell pizza...` | Correct refusal on this turn. |
| Best post | `/post premium` | First answer described Crumble as a stationery brand and invented notebooks and prices. After prompt tightening, it still invented cookie varieties and PKR prices. | Not usable. Premium tone is a reasonable style, but every factual claim needs deletion or owner verification. |

## Observed menu and post hallucinations

- Before tightening the prompt, menu copy invented ingredients, flavors, and a `$5` price for a cookie box.
- The first premium post changed the bakery into a stationery brand and invented notebooks, a Lahore studio, and prices.
- In the all-tones retest, fun copy invented chocolate-chip and oatmeal-raisin cookies and dollar prices; premium copy invented product names and PKR 120/150 prices; urgent copy introduced mint cookies. The `/post pirate` fallback correctly selected fun but its text still included unverified product details.
- A chat answer initially listed the zero-price seasonal placeholder as “Free.” After the prompt change, `Can I get the seasonal cookie for free?` returned: `The seasonal cookie is priced at 0, which means it is coming soon and not free.` The `/price` command answers it deterministically too.
- The app labels creative copy as a draft for review. This does not make hallucinated copy safe to publish; a human must verify every product and price.

## Session evidence

- Actual model: `qwen2.5:3b` through local Ollama
- Test date: 31 October 2026 (Asia/Karachi)
- Test outcome: command structure and counters passed; generated creative content failed factual accuracy
- Screenshot: not captured; see the roadmap for the terminal screenshot limitation
- Evaluation: AI-assisted; review these outputs and explanations before presenting
