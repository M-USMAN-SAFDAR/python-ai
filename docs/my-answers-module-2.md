# Module 2 Quick Check Reference Answers

**Preparation:** AI-assisted study answers and output predictions, prepared after implementation. The professor's quick checks instruct students to answer independently before consulting notes or AI; these answers are not represented as an independent timed attempt. Review the explanations and make your own attempt before class.

## Checkpoint 1: lessons 2.1–2.4

2.1: Q1 **b**, Q2 **b**, Q3 **b**, Q4 **a**, Q5 **b**, Q6 `200 tokens in 3.5 seconds`

- Change the model name/provider to switch LangChain backends. The invocation result text is in `.text`. Low temperature suits predictable facts; a connection refusal means first check that Ollama is running. Streaming reveals output as it is generated. The usage dictionary has 200 total tokens, and 3.5 billion nanoseconds are 3.5 seconds.

2.2: Q1 **b**, Q2 **b**, Q3 **b**, Q4 **a**, Q5 **b**, Q6 `['sys', 'u2', 'a2', 'u3'] 6`

- Negative list indices count from the end. `.append()` mutates a list and returns `None`. A model only sees sent history; keep the system message when trimming. Unbounded history increases prompt cost and can exceed context. The source list remains length 6.

2.3: Q1 **b**, Q2 **c**, Q3 **b**, Q4 **b**, Q5 **b**, Q6 `{'cupcake': 7, 'brownie': 0, 'donut': 8} 3 True`

- `.get(key, default)` avoids a missing-key error; direct indexing raises `KeyError`. Add keys with assignment. Nested dictionaries are indexed one key at a time. Ground answers in business data. The cupcake count becomes 7, donut is added, and brownie remains a key even though its value is zero.

2.4: Q1 **b**, Q2 **b**, Q3 **b**, Q4 **b**, Q5 **b**, Q6 `2: complaint` then `3`

- `range` stops before its end. `.items()` supplies key/value pairs. Because `total = 0` is inside the loop, the final iteration leaves it at 300. `continue` skips the current item. Create the model once before looping. The empty review at position 3 is skipped before the count increment.

## Checkpoint 2: lessons 2.5–2.8

2.5: Q1 **c**, Q2 **b**, Q3 **b**, Q4 **b**, Q5 **b**, Q6 `Total: 1100.0` then `None`

- A function without `return` returns `None`. Required parameters cannot follow defaulted parameters. Call a function with parentheses and its inputs. The named `lines=2` argument selects the desired default override. Share repeated AI request code in one helper. `show()` prints the total but returns no value.

2.6: Q1 **c**, Q2 **b**, Q3 **b**, Q4 **b**, Q5 **b**, Q6 `Skipped abc` then `550`

- Append mode preserves existing log entries. `ensure_ascii=False` keeps non-English text readable. Bare `except` hides unrelated bugs. A connection error means the local service cannot be reached. Runtime chats and logs may contain private data. The invalid integer is skipped; 250 + 300 equals 550.

2.7: Q1 **b**, Q2 **b**, Q3 **b**, Q4 **b**, Q5 **b**, Q6 `CHECK: pizza is not on the menu` then `500 (missing)`

- Temperature zero is chosen for repeatability, though it cannot guarantee identical outputs. The schema constrains shape, not factual correctness. Flag names that do not appear in the source. Python uses the actual price dictionary for totals. Invalid JSON raises `json.JSONDecodeError`. The pizza line is skipped; cupcake total is 2 × 250; no address exists.

2.8: Q1 **b**, Q2 **b**, Q3 **b**, Q4 **b**, Q5 **c**, Q6 prints `step 0: tool`, `step 1: tool`, `step 2: tool`, then `Gave up: a human will help`

- Tool names and docstrings describe the available actions. A decorated LangChain tool can be invoked with `.invoke({...})`. Tool results must include the matching `tool_call_id`. `MAX_STEPS` bounds repeated calls. Actions that change data need human approval. The loop exhausts its three tool-only replies and runs the `else` block.

**Source:** [Checkpoint 1 quick checks](https://github.com/the-schoolofai/python-ai/blob/main/docs/assessments/module-2/checkpoint-1-quick-checks.md) · [Checkpoint 2 quick checks](https://github.com/the-schoolofai/python-ai/blob/main/docs/assessments/module-2/checkpoint-2-quick-checks.md)
