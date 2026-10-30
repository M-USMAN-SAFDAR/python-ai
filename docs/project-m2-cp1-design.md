# Module 2 Checkpoint 1: Content Studio Design

Business context: Crumble Pakistan is used as an independent student case study. The business has not supplied or approved this data. The prices below are demo values only and must not be presented as current company prices.

## Facts

| Key | Value | Status |
|---|---|---|
| name | Crumble Pakistan | Public brand name used for case study |
| type | Cookie bakery | Publicly described business type |
| city | Lahore | Case-study location, not headquarters claim |
| audience | University students and families | Exercise assumption |
| hours | Not supplied; confirm with business | Unknown |
| delivery | Not supplied; confirm with business | Unknown |
| prices | Chocolate cookie 250; double chocolate cookie 300; cookie box 1200; gift box 1800 PKR | Demo-only assumptions |
| coming soon | Seasonal cookie, price 0 | Exercise placeholder |

## Tones

| Tone | Description sent to AI |
|---|---|
| fun | Playful, cheerful, and brief |
| premium | Elegant and calm without unverified claims |
| urgent | Energetic but not pushy; no invented deadlines or scarcity |

## Model selection

| Job | Model and temperature | Why |
|---|---|---|
| Menu descriptions | Qwen 2.5 3B, creative 0.8 | Marketing text benefits from variety |
| Social posts | Qwen 2.5 3B, creative 0.8 | Chosen tone needs expressive wording |
| Customer chat | Qwen 2.5 3B, precise 0.2 | Grounded answers should be steady and concise |
| Prices | Python dictionary | Exact data needs no AI call |

## Feature test results

| Input | Expected | Result |
|---|---|---|
| `/menu` | Skip zero-price item; number the rest; format prices with commas | Pass; AI copy itself contained invented claims, documented in results |
| `/post fun`, `/post premium`, `/post urgent` | Stream one post for each tone | Streamed; content quality failed with invented products/prices |
| `/post pirate` | Use fun default without a KeyError | Pass for fallback; generated content still hallucinated |
| `/price COOKIE BOX` | Return dictionary price without an AI call | Pass: 1,200 PKR |
| `/price seasonal cookie` | Say coming soon | Pass |
| `/price pizza` | Say not on menu | Pass |
| `My name is Ali`, then `What is my name?` | Memory keeps the name | Pass |
| `/reset`, then `What is my name?` | Cleared memory no longer has the name | Pass |
| Press Enter | Ask again | Pass |
| `BYE` | Print goodbye and full session report | Pass; report included counts, token total, and elapsed seconds |

## AI quality evaluation

Live output and hallucination checks belong in [project-m2-cp1-results.md](project-m2-cp1-results.md). No model output is recorded there until a real local model call succeeds.
