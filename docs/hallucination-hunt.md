# Module 2 Lesson 2.7: Hallucination Hunt

The assignment's extraction messages are synthetic test data. Live model results have not yet been collected, so this report does not claim an observed hallucination.

Run `uv run lesson_2_7_extractor.py` from `code/`, then record one real extraction that was wrong or uncertain, which validation caught it, and any correction made. Required checks in the script include off-menu items, quantities, missing or invented customer names, and valid JSON. Totals are calculated from the Python price dictionary rather than model output.

| Case | Actual model output | Check raised | Fix/result |
|---|---|---|---|
| Off-menu item | Pending live run | Item not on menu | It is not priced or saved |
| Non-order question | Pending live run | N/A | Routed to human reply |
| Name not present in message | Pending live run | Customer name not in source text | Not saved |
