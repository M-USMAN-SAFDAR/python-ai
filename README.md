# Python for AI — Muhammad Usman Safdar

My learning portfolio for **Python for AI**, following the School of AI course.

**Goal:** Become an AI Agent Developer who builds useful tools for small businesses.
**GitHub:** https://github.com/M-USMAN-SAFDAR/python-ai
**Local model:** `qwen2.5:3b` through Ollama.

## Run

Install uv and use Python 3.13. From this folder:

```powershell
uv sync
uv run main.py
uv run code/lesson_01_intro.py
uv run code/lesson_02_toolkit.py
uv run code/lesson_04_print_input.py
uv run code/lesson_05_variables.py
uv run code/lesson_06_strings_prompts.py
```

For number questions, enter whole numbers without commas, e.g. `15000`. The scripts intentionally use beginner-level straight-line code; invalid numeric text raises ValueError.

## Lessons implemented and run

| Lesson | Work |
|---|---|
| 1.1 | Career introduction and example business problem |
| 1.2 | Actual toolkit versions and real Qwen conversation |
| 1.3 | uv project, lockfile, clean folders and README |
| 1.4 | Business prompt builder with budget stretch |
| 1.5 | Model types, practice token cost and monthly estimate |
| 1.6 | Prompt cleaner, 150-character question limit and formatting |

See [actual script runs](docs/script-runs.md), [toolkit evidence](docs/setup-check.md), [first Ollama chat](docs/ollama-first-chat.md), and [model notes](docs/model-notes.md).

![Toolkit versions](docs/setup-check.png)

## Module 1 Project: AI Prompt Kit

A Python tool that turns business details into three ready-to-use AI prompts, plus a bonus WhatsApp enquiry prompt.

**Run:** `uv run code/project_m1_prompt_kit.py`

![Prompt Kit running](docs/project-m1-run.png)

The student-supplied screenshot shows the three required prompts from a separate run with a 1500 PKR budget and university students as the audience. The saved AI tests use 15000 PKR and university students and families. The bonus fourth prompt is outside the screenshot.

**Who would pay for this:** Small business owners who need help drafting specific AI prompts for marketing and customer service.

See [actual Qwen test results and honest evaluations](docs/project-m1-results.md), [run transcript](docs/project-m1-run.txt), and [demo preparation](docs/module-1-study-guide.md).

Sweet Crumbs is a **fictional demonstration**, not a real client. Real-business testing remains to be done. Generated content contains errors documented in the evaluations and needs review before use.

## Submission status

- Scripts and model responses were prepared and tested with AI assistance.
- The model profile's price is fictional arithmetic practice, not Ollama billing.
- Independent Quick Check answers remain blank; [reference answers](docs/module-1-reference-answers.md) are separate study material.
- Student-supplied genuine screenshots are saved in `docs/setup-check.png` and `docs/project-m1-run.png` and displayed above.
- A real business test and the student's three-minute live demo remain pending.
- Review and understand every line before presenting this work.

Course reference: https://github.com/the-schoolofai/python-ai
