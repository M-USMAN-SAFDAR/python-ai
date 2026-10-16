# Module 1 explanation and demo preparation

AI assistance was used to prepare this repository. Review the code and make sure you can explain it before submitting.

## Explain the code

- `name = "Muhammad Usman Safdar"`: assign a text value to a variable.
- `input("City: ")`: display a question and return the answer as text.
- `int(input(...))`: convert text to a whole number. `15000` works; `15,000` or `abc` raises ValueError.
- `f"Hello {name}"`: insert a variable into text.
- Triple quotes: create a multiline string; at the start of the file this is a module docstring.
- `#`: a comment Python ignores, used here to explain choices.
- `type(value)`: show whether a value is str, int, float, bool, or NoneType.
- `tokens / 1000 * price`: calculate cost at a rate per 1,000 tokens.
- `round(cost, 2)`: round a number; `:.2f` displays exactly two decimal places.
- `.strip()`: return a new string without whitespace at either end.
- `.title()` and `.capitalize()`: return new strings with altered casing.
- `len(question)`: count characters, including spaces.
- `question[:150]`: keep at most the first 150 characters.
- `'python' in question.lower()`: check for Python regardless of case.
- `.replace(...)`: return text with matching substrings replaced.
- `"=" * 60`: repeat a character to make an output separator.

## Three-minute demo outline

0:00–0:30: Explain that a business could use a tool for writing useful AI prompts. Introduce Crumble Pakistan as an independent student case study, based on public information and assumed audience and budget, without company involvement.

0:30–1:30: Run `uv run code/project_m1_prompt_kit.py`. Enter the five details from crumble-business-profile.md. Show the three required prompts and the bonus WhatsApp prompt.

1:30–2:30: Show one actual Qwen result in project-m1-results.md. Explain one useful part and any invented or unverified claims. Do not describe model-generated claims as verified company facts.

2:30–3:00: Explain how you could adapt this for a real shop. A future version could call Ollama automatically and validate the budget. Explain one code line in your own words.

## Quick Checks

Try the questions yourself, then use the separate reference answers to review. Reference answers are AI-assisted study material, not a record of your independent attempt.
