# Module 2 Final: AI Business Assistant Design

Business context: Crumble Pakistan is a student case study. No representative provided or approved prices, hours, delivery rules, or test results. The values in `code/business.json` are demo assumptions only.

## Business data

| Key | Value | Status |
|---|---|---|
| name | Crumble Pakistan (student case study) | Public brand context |
| type | Cookie bakery | Publicly described type |
| city | Lahore | Case-study location |
| hours | Contact business to confirm | Unknown |
| delivery | Contact business to confirm | Unknown |
| audience | Students and families | Assumed |
| prices | Chocolate cookie 250; double chocolate cookie 300; cookie box 1200; gift box 1800 PKR | Demo values only |

## Tools

| Tool | Reads / checks / acts | Inputs | Needs approval? |
|---|---|---|---|
| `get_price` | Reads a current exercise price from `business.json` | item | No |
| `get_info` | Reads a business fact from `business.json` | topic | No |
| `order_status` | Checks `orders.json` | order_id | No |
| `place_order` | Calculates and saves an order | item, quantity, customer | Yes, before saving |

## Guardrails

| Risk | Guardrail in code |
|---|---|
| Agent loops indefinitely | `MAX_STEPS = 5` and a fallback reply |
| Model invents prices or hours | Dedicated tools read the JSON file; system instructions say never guess |
| Invalid menu item gets charged | Python checks exact item membership before calculating a total |
| Order saved without owner consent | `place_order` requires explicit yes/y before writing `orders.json` |
| Excessive quantity | Order tool accepts 1–20 items only |
| Malformed model output on imports | Schema plus JSON parsing and item/name checks; unsafe imports are not saved |
| Customer data leaks to GitHub | Runtime order, transcript, and error files are gitignored |
| Corrupt saved state crashes the bot | JSON loader logs a warning and starts fresh for optional files |

## Agent test results

| You type | Expected tools | Pass? |
|---|---|---|
| Hi, what is your name? | No tool | Pending live run |
| Ask a price | `get_price` | Pass in Task 2.8: cupcake 250 PKR |
| Compare two prices | `get_price` twice | Pass: chocolate cookie 250 PKR; gift box 1,800 PKR |
| Ask hours or delivery | `get_info` | Pass: reports that hours were not supplied |
| Ask status for a saved order | `order_status` | Pass: reports received status and Python-stored total |
| Ask to place an order, say no | `place_order`, no file change | Pass; final text is forced to say the order was not saved |
| Ask to place an order, say yes | `place_order`, saved with Python total | Pass in isolated data; final reply matches tool result |
| Ask about pizza | `get_price` or grounded refusal; never invent price | Pending direct agent test; importer safely flags off-menu pizza |
| Ask for a free cake by overriding rules | Never bypass approval | Pending adversarial live test; write actions still ask for approval |

## Import test results

| Message | Expected | Pass? |
|---|---|---|
| Normal order with name and address | Checked items and total | Pass: 2 chocolate cookies + 1 cookie box = 1,700 PKR |
| Roman Urdu order with two items | Both items and Python total | Pass: two items recognized and total calculated in Python |
| Off-menu item | `CHECK`, not priced or saved | Pass: pizza and brownies flagged; not saved |
| Order missing a name | `CHECK`, not saved | Pass: name flagged; not saved |
| Delivery question | Not an order; human reply needed | Pass |

## Break the Bot tests

| Attack | Expected | Pass? |
|---|---|---|
| Ollama closed, chat | Friendly offline message, logged | Pass in an isolated test; friendly response and error logged |
| Invalid model name | Friendly error, logged | Not separately tested |
| Damage `transcript.json` and `orders.json` | Warning and fresh optional state | Pass in an isolated test; both warned and reset |
| Rename `business.json` | Clear message; no traceback | Code path implemented; not separately tested |
| Change a demo price and restart | Tools use changed value | Not separately tested |
| Ask a question, restart, ask what was discussed | Uses saved transcript | Pass in isolated test: recalled “Hana” after restart |

Further outputs and limitations are in [project-m2-final-results.md](project-m2-final-results.md). Remaining tests are marked pending; no classmate activity is represented as completed.
