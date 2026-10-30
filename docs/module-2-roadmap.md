# Module 2 Roadmap

This project currently contains my Module 1 work through lessons 1.1–1.6 and the first Module 1 project (AI Prompt Kit). The professor's current repository extends Module 1 through lessons 1.7–1.8, then Module 2 through 2.8. Before starting Module 2 project work, check whether the class has assigned or expects the remaining Module 1 lessons.

Course source: [the-schoolofai/python-ai](https://github.com/the-schoolofai/python-ai)

## Module 2 sequence

| Lessons | Main concepts | Task/project outcome |
|---|---|---|
| 2.1–2.4 | Real model calls, message history, dictionaries and facts, loops | AI tutor, memory tutor, grounded persona bot, batch product writer; then AI Content Studio |
| 2.5–2.8 | Functions, files and JSON, structured output, tools and agent loops | Reusable AI skills, persistent bot, checked order extraction, first business agent |

Official lesson readings: [2.1 First AI Call](https://github.com/the-schoolofai/python-ai/blob/main/docs/02-talk-to-ai/2.1-your-first-ai-call.md) · [2.2 Chat History](https://github.com/the-schoolofai/python-ai/blob/main/docs/02-talk-to-ai/2.2-chat-history-with-lists.md) · [2.3 Dictionaries and Facts](https://github.com/the-schoolofai/python-ai/blob/main/docs/02-talk-to-ai/2.3-messages-are-dictionaries.md) · [2.4 Loops](https://github.com/the-schoolofai/python-ai/blob/main/docs/02-talk-to-ai/2.4-loops-that-talk.md) · [2.5 Functions](https://github.com/the-schoolofai/python-ai/blob/main/docs/02-talk-to-ai/2.5-functions-reusable-ai-skills.md) · [2.6 Files and JSON](https://github.com/the-schoolofai/python-ai/blob/main/docs/02-talk-to-ai/2.6-files-json-and-errors.md) · [2.7 Structured Output](https://github.com/the-schoolofai/python-ai/blob/main/docs/02-talk-to-ai/2.7-structured-output.md) · [2.8 First Agent](https://github.com/the-schoolofai/python-ai/blob/main/docs/02-talk-to-ai/2.8-your-first-agent.md)

The course's Module 2 Checkpoint 1 project combines the first four lessons: generate menu descriptions in a batch, stream social posts, answer prices from a dictionary without spending tokens, chat with bounded memory grounded in business facts, and print a session report. Its required script is `code/project_m2_content_studio.py`.

## Local setup and first task

The professor's README recommends Ollama with `llama3.2` (or `llama3.2:1b` for a smaller model) and these project packages:

```powershell
ollama pull llama3.2
uv add langchain langchain-ollama
```

The packages are now recorded in `pyproject.toml` and `uv.lock`. This workspace has Python 3.13.15, and the `qwen2.5:3b` Ollama model was available for real lesson and project runs. On this machine, set `OLLAMA_HOST=127.0.0.1:11434` if your environment has an unusual Ollama host override; a normal Ollama install typically uses its default local endpoint.

Task 2.1 is `code/lesson_2_1_first_ai_call.py`. It asks for a topic and learner level, sends a system and user message through LangChain to local Ollama, then prints the answer, token count and elapsed seconds. This project uses the already documented `qwen2.5:3b` model name; if that model is unavailable locally, use a model shown by `ollama list` or pull one first.

## Recommended work order

1. Finish each lesson and its individual task (2.1 through 2.4) before combining concepts.
2. Keep using Crumble Pakistan as the example business. Treat unverified hours, prices, delivery terms and product facts as placeholders until you have real owner-approved information.
3. Build the Checkpoint 1 design tables and feature-test checklist before coding the Content Studio.
4. In Module 2 Checkpoint 2, upgrade the studio with functions, JSON persistence, structured output, and tools with owner approval.
5. Capture real model outputs and record failures or unsupported facts honestly; AI responses and token counts vary by run.

The course says to commit each task separately and commit `pyproject.toml` and `uv.lock` with dependency changes. Understand each line before presenting it.

## Work completed in this repository

The scripts for tasks 2.1–2.8 and both checkpoint projects have been added. Real local model calls were made for the lesson tasks and projects. Test tables and observed model failures are recorded in the project design/results files. AI-generated creative copy was inaccurate even after tightening the prompts, so treat it as an unapproved draft.

## Student/classroom items still required

- Take the timed quick checks independently first; the repository answer sheet is explicitly labelled as AI-assisted study material.
- Read and understand the lessons, then explain the code in your own words.
- Ask a classmate to run Task 2.6's Break the Bot and record their feedback.
- Practise and deliver the checkpoint demos in class.
- Capture the professor-required screenshots from the live terminal runs. The terminal screenshot was not automated in this environment.
- Confirm exercise facts/prices with the business before presenting them as real; current values are marked as demo assumptions.
