# Module 1 Quick Check Answers

**Student:** Muhammad Usman Safdar

**Preparation:** AI-assisted answers based on the supplied lessons. This is not an independent timed attempt or a claim that the student has mastered the material.

## Module 1 quiz (lessons 1.1–1.4)

1.1: Q1 b, Q2 c, Q3 b, Q4 c, Q5 b, Q6 `Hello from kimi!`

1.2: Q1 c, Q2 b, Q3 b, Q4 b, Q5 b, Q6 `Python 3.13.16`

1.3: Q1 b, Q2 c, Q3 b, Q4 b, Q5 b, Q6 `Hi, I am Ali and I will become an AI Agent Developer.`

1.4: Q1 c, Q2 b, Q3 c, Q4 b, Q5 c, Q6 `201`

### Explanations

- **1.1:** Agents plan, use tools and repeat a loop. LLMs predict tokens. The formula is LLM + Tools + Memory + Loop. Applied GenAI uses existing models for business tasks. A confidently false generated answer is a hallucination.
- **1.2:** uv manages Python and projects. Restarting a terminal refreshes PATH. Stable Python versions improve library compatibility. Ollama runs models locally. GitHub attributes commits using a verified email. Q6 assumes Python 3.13.16; this machine's installed project Python is 3.13.15.
- **1.3:** Lockfiles record exact dependency versions. Ignore .venv. Simple scripts need no build system. `uv add ollama` adds the dependency. `uv run` uses the project environment. F-strings insert variable values into text.
- **1.4:** input returns str. sep joins print arguments with the chosen separator. F-strings format numbers into text. Comments explain why. Invalid integer text raises ValueError. `"20" + "1"` concatenates to `"201"`.

## Short Quick Checks inside the lessons

### Lesson 1.1

1. A chatbot responds to a message; an agent can plan, use tools and repeat steps toward a goal.
2. GenAI lets beginners build applications with existing models before learning the maths and infrastructure needed to train models.
3. A local shop could use an AI-assisted FAQ drafting tool to help staff answer repeated customer questions.

### Lesson 1.2

1. uv manages Python installations, environments and dependencies together; pip primarily installs packages.
2. Close and reopen the terminal to load the updated PATH.
3. A clinic handling sensitive information could prefer local Ollama inference. The surrounding application must also keep that information local.

### Lesson 1.3

1. uv.lock records resolved dependency versions for repeatable installations. It does not guarantee identical behaviour on every platform.
2. .venv is generated and machine-specific. Others recreate it with uv instead of downloading it through Git.
3. Run `uv run main.py`, then `uv run lesson_01_intro.py` from code/. Both should succeed.

### Lesson 1.4

1. input returns a string (`str`).
2. Use `print(f"Tokens: {50}")`.
3. F-strings insert user values into prompt templates so one template works for different users and businesses.

### Lesson 1.5

1. `int(3.9)` returns `3`: truncation rather than rounding.
2. input returns text, so multiplying by 2 repeats the text. Use `price = float(input("Price: "))` for numeric multiplication in this exercise.
3. `2nd_model` is invalid because names cannot start with a digit. Use `second_model` or `model_2`.

### Lesson 1.6

1. `"Python for AI"[-2:]` returns `"AI"`.
2. Membership is case-sensitive. Use `"refund" in message.lower()`.
3. Strings are immutable. `name.strip()` returns a new value without updating name. The original `" ali "` has five characters. Assign `name = name.strip()` to keep the result.

## Output verification

These output answers were recorded before this turn's verification run, then checked with the project's uv environment. The version question uses its stated hypothetical version. These AI-assisted answers are review material, not evidence of an independent student prediction.
