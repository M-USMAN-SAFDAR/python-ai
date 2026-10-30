# Module 2 Final: AI Quality Results

Local Ollama `qwen2.5:3b` was used for real tool and import runs. All business prices remain demo assumptions. Test excerpts are from separate runs; synthetic orders were created both in the ignored `code/` runtime files and in isolated temporary directories. The ignored local order/transcript/log files are exercise data, not customer records.

| Test | Actual answer or extraction | What the code caught | Follow-up change |
|---|---|---|---|
| Agent answer: hours | “The business hasn't provided their hours yet. You'll need to contact them to find out when they're open.” | `get_info` returned “not supplied”; no hours were invented. | Correct. |
| Agent answer: compare prices | Chocolate cookie 250 PKR; gift box 1,800 PKR. | Two `get_price` calls; amounts came from the dictionary. | Correct for exercise values. |
| Order approval: decline | “The order was not placed or saved because the owner did not approve it.” | `place_order` returned not saved; code overrides contradictory model copy. | Correct after postprocessing fix. |
| Order approval: accept | `Order A102 placed: 1 x gift box, total 1,800 PKR` | Owner typed yes; Python calculated and saved. Final answer matches tool result. | Correct for exercise values. |
| WhatsApp import: Roman Urdu | 2 chocolate cookies + 1 cookie box; Ali; 1,700 PKR. | Menu and name/address checks passed. Owner approved; saved in isolated data. | Correct for the message and demo prices. |
| WhatsApp import: off-menu | Pizza and brownies flagged as not on menu; total 0; not saved. | Unknown items never priced; unsafe order not offered for approval. | Correct. |
| WhatsApp import: missing name | 1 chocolate cookie + 2 gift boxes; total 3,850 PKR; customer name missing; not saved. | Name check blocked saving. | Correct; human follow-up required. |
| WhatsApp import: not an order | “Not an order: this message needs a human reply.” | Model marked it not an order; no save. | Correct. |
| Chat across restarts | Second run answered “Your name is Hana.” | Plain user/assistant dictionaries were loaded from `transcript.json` and sent as history. | Pass in isolated data. |

## Demo evidence

- Model: `qwen2.5:3b` through local Ollama
- Test date: 31 October 2026 (Asia/Karachi)
- Runtime checks: tools, approval, saved orders, good and unsafe imports, damaged JSON recovery, offline handling
- Screenshot: not captured; see the roadmap for the terminal screenshot limitation
- Evaluation: AI-assisted; review the output and code before presenting
