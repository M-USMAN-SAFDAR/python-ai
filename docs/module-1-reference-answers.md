# Module 1 reference answers — AI-assisted study material

These are explanations for revision, not a claim that I independently attempted the quiz.

| Lesson | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 |
|---|---|---|---|---|---|---|
| 1.1 | b | c | b | c | b | `Hello from kimi!` |
| 1.2 | c | b | b | b | b | `Python 3.13.16` (the question's stated version) |
| 1.3 | b | c | b | b | b | `Hi, I am Ali and I will become an AI Agent Developer.` |
| 1.4 | c | b | c | b | c | `201` |

1.1: Agents combine an LLM, tools, memory and a loop. LLMs predict tokens; confidently false generated claims are hallucinations.

1.2: uv manages Python and projects; restart a terminal after installation to refresh PATH. Ollama can run locally. Matching a verified GitHub email attributes commits to a profile. The quiz version differs from this machine's installed Python 3.13.15.

1.3: uv.lock records resolved versions. Ignore .venv. Simple scripts need no build system. `uv add` manages dependencies; `uv run` selects the project environment.

1.4: input returns str. `sep="-"` joins print arguments with hyphens. F-strings format numbers into text. A useful comment explains why. Invalid integer text raises ValueError. `"20" + "1"` concatenates to `"201"`.

## Lesson 1.5 short check

1. `int(3.9)` returns `3`: truncation, not rounding.
2. input returns text, so `price * 2` repeats the text. Use `float(input("Price: "))` for decimal arithmetic in this exercise.
3. `2nd_model` is invalid because it starts with a digit. Use `second_model`.

## Lesson 1.6 short check

1. `"Python for AI"[-2:]` returns `"AI"`.
2. Membership is case-sensitive. Use `"refund" in message.lower()`.
3. Strings are immutable. `name.strip()` returns a new value without changing name; assign `name = name.strip()` to retain it.
