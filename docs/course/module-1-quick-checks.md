# Module 1 Quick Checks (Lessons 1.1 to 1.4)

**Course:** Python for AI · **Module 1:** Python Basics for GenAI and Agentic AI · **Updated:** Oct 2026

> **Student version.** Answer on your own first, without AI tools or notes. The goal is to find what you have not understood yet, not to get full marks.

**Format per lesson:** 5 MCQs + 1 "Predict the Output" · **Time:** 5 minutes · **Marks:** 6 per lesson

**How to answer:** write your answers in a file `docs/my-answers-module-1.md` like this:

```text
1.1: Q1 b, Q2 c, Q3 ..., Q6 Hello ...
```

**Predict the Output rule:** write your answer **before** running the code. Then run it with `uv run` and check yourself.

---

## Lesson 1.1: Welcome to the GenAI & Agentic AI

**Q1.** Which best describes **Agentic AI**?
- a) A chatbot that gives one reply to one question
- b) AI that plans, uses tools and acts in a loop until a goal is done
- c) Software that trains new AI models from scratch
- d) AI that only generates images

**Q2.** At its core, a Large Language Model (LLM) works by:
- a) Searching Google for every answer
- b) Following rules written by programmers
- c) Predicting the next token
- d) Copying answers from a fixed database

**Q3.** Complete the formula: **Agent = LLM + Tools + Memory + ______**
- a) Database
- b) Loop
- c) Internet
- d) GPU

**Q4.** Why does this course start with GenAI instead of ML / DL?
- a) ML and DL are no longer used
- b) Python cannot do ML
- c) Most businesses use ready-made models through APIs, so applied AI skills are in demand
- d) GenAI does not need any programming

**Q5.** An AI gives a confident answer that is completely wrong. This is called:
- a) A token
- b) A hallucination
- c) A prompt
- d) A context window

**Q6. Predict the Output**
```python
model = "kimi"
print(f"Hello from {model}!")
```

---

## Lesson 1.2: Setting Up Your AI Dev Toolkit

**Q1.** Which tool can install **Python itself** and also manage packages and projects?
- a) pip
- b) Git
- c) uv
- d) VS Code

**Q2.** You installed uv, but the terminal says `uv: command not found`. What should you try **first**?
- a) Reinstall Windows
- b) Close and reopen the terminal
- c) Install pip
- d) Delete the project

**Q3.** Why does the course use Python 3.13 instead of the newest version?
- a) Newer versions are paid
- b) AI libraries need time to support new versions, so pros use a stable one
- c) 3.13 is the only version uv supports
- d) Newer versions do not have `print()`

**Q4.** A clinic does not want patient data sent to the cloud. Which tool lets you run AI models **locally**?
- a) GitHub
- b) Ollama
- c) Antigravity
- d) pip

**Q5.** Why should your `git config` email match your GitHub account email?
- a) Git will not install otherwise
- b) So your commits are linked to your GitHub profile
- c) To make code run faster
- d) It is required by Python

**Q6. Predict the Output**
Your project uses Python 3.13.16. What does this print?
```bash
uv run python --version
```

---

## Lesson 1.3: Your First Python Project with uv

**Q1.** What does `uv.lock` do?
- a) Locks your laptop
- b) Stores exact package versions so the project runs the same on any machine
- c) Stores your GitHub password
- d) Prevents others from editing your code

**Q2.** What should happen to the `.venv/` folder?
- a) Upload it to GitHub so others can use it
- b) Email it to the client
- c) Keep it out of GitHub (it is in `.gitignore`)
- d) Delete it after every run

**Q3.** After removing `src/` and `[build-system]` from `pyproject.toml`, what happens?
- a) The project stops working
- b) The project becomes a simple project, and scripts still run with `uv run`
- c) Python is uninstalled
- d) Git history is deleted

**Q4.** Which command correctly adds the `ollama` package to your project?
- a) `pip install ollama`
- b) `uv add ollama`
- c) `git add ollama`
- d) `python ollama`

**Q5.** Why do we run code with `uv run` instead of plain `python`?
- a) It is shorter to type
- b) It always uses the project's own `.venv`, even if you forgot to activate it
- c) It uploads the code to GitHub
- d) It makes the code run on the GPU

**Q6. Predict the Output**
```python
name = "Ali"
goal = "AI Agent Developer"
print(f"Hi, I am {name} and I will become an {goal}.")
```

---

## Lesson 1.4: Talking to Python: print, input and Comments

**Q1.** What data type does `input()` always return?
- a) int
- b) float
- c) str
- d) It depends on what the user types

**Q2.** What does this print?
```python
print("Python", "for", "AI", sep="-")
```
- a) `Python for AI`
- b) `Python-for-AI`
- c) `Python - for - AI`
- d) `PythonforAI`

**Q3.** `print("Tokens: " + 50)` gives an error. Which line fixes it?
- a) `print("Tokens: " - 50)`
- b) `print(Tokens: 50)`
- c) `print(f"Tokens: {50}")`
- d) `print("Tokens: " + "fifty" + 50)`

**Q4.** Which is the **best** comment?
- a) `temperature = 0.2  # set temperature to 0.2`
- b) `temperature = 0.2  # low value for focused, factual answers`
- c) `temperature = 0.2  # temperature`
- d) `temperature = 0.2  # code`

**Q5.** The user types `abc` into `int(input("Age: "))`. Which error appears?
- a) SyntaxError
- b) NameError
- c) ValueError
- d) No error

**Q6. Predict the Output**
The user types `20`.
```python
age = input("Age: ")
print(age + "1")
```

---

## After the Check

- Answers are discussed in the **next class warm-up**.
- Got a question wrong? Re-read that lesson's section in `docs/` and redo its Code Task.
- Commit your answers file: `git commit -m "Module 1 quick checks"`

**Self-score guide**

| Score (per lesson) | Meaning |
|---|---|
| 6 | Mastered, move on |
| 4 to 5 | Good, review what you missed |
| 0 to 3 | Re-read the lesson and ask in class |
