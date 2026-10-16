# Verification — 16 October 2026

All seven runnable scripts passed `uv run` from the repository root. The introduction also passed when run from `code/`, as requested in Task 1.3.

Additional checks passed:

- Model profile shows the four required types; 1000 tokens at 0.50 PKR per 1K and 20 chats/day gives 0.50 PKR/chat and 300 PKR for 30 days (practice pricing).
- Cleaner normalises the name, detects Python without case sensitivity, replaces the sample word, and limits a long submitted question to exactly 150 characters.
- Project substitutes Crumble details correctly and also runs with different business details and a zero budget.
- Project has exactly five inputs, a docstring, at least three why comments, four f-string prompts, and no loops, conditionals or functions.
- No src folder or build-system/project.scripts sections. No tracked .venv.
- All required project prompts have actual Qwen responses and evaluations. The growth response now finishes normally; its missing budget breakdown and other limitations are explicitly evaluated.

Invalid numeric input still raises ValueError by design at this lesson level. No claim is made that these beginner scripts validate all user input.
