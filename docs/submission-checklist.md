# Module 1 requirement audit

Audited on 16 October 2026 against the professor's message and the nine supplied documents in [course/](course/). This covers the supplied lessons 1.1–1.6, not future course modules.

## Professor's mission

| Requirement | Status and evidence |
|---|---|
| Own repository named python-ai | Present; GitHub API confirmed public, default branch main: https://github.com/M-USMAN-SAFDAR/python-ai |
| Commit every small effort | Separate commits for tasks, project, fixes, screenshots and this audit. Actual commit dates are preserved. A future daily streak requires continuing work; no dates were fabricated. |
| Read lessons in docs | All six supplied lessons now included unchanged in docs/course with attribution and a reading index. The student must do the reading. |
| Do Quick Checks | Completed AI-assisted answers for the 1.1–1.4 quiz and all six lesson short checks are in my-answers-module-1.md, committed as `Module 1 quick checks`. This does not represent an independent student attempt. |
| Complete Code Tasks | Implemented and run; details below. |
| On-time submissions / leaderboard / classmates | Deadlines and leaderboard rules beyond the supplied text are not available. On-time status, participation and helping classmates cannot be certified from these files. |

## Lesson requirements

| Task | Status and evidence |
|---|---|
| 1.1: name, goal, problem variables; f-strings; why line | Present in code/lesson_01_intro.py; reason is the final output line. City is clearly labelled as an example, not the student's confirmed hometown. |
| 1.2: six versions and screenshot | Present in code/lesson_02_toolkit.py, docs/setup-check.md and docs/setup-check.png. Claude's full executable path works even though it is missing from this terminal's PATH. |
| 1.2: Ollama question, answer, model and review | Present in docs/ollama-first-chat.md with actual qwen2.5:3b evidence. The model's failure to return two lines is acknowledged. |
| 1.3: code, notebooks, docs, metadata, main, README and lockfile | Present. notebooks/.gitkeep preserves its empty folder; docs is populated and needs no .gitkeep. |
| 1.3: no src, build-system or project.scripts; ignore .venv | Verified. Both root main.py and intro from code/ run with uv. |
| 1.3: README name, course, goal, run command and lesson list | Present. There is no assigned standalone lesson_03 script; this task is repository setup. |
| 1.4: inputs, welcome, required prompt, docstring, why comments | Present in code/lesson_04_print_input.py. Budget conversion and actual prompt-test.md satisfy the stretch; the model's truncated answer is documented honestly. |
| 1.5: four types, f-strings/type(), int input, rounded cost, comments | Present in code/lesson_05_variables.py. Thirty-day cost stretch included. Price explicitly fictional; model context source in model-notes.md. |
| 1.6: name/question cleaning, lengths/tokens, Python detection, multiline prompt with 150-character limit | Present in code/lesson_06_strings_prompts.py. Docstring, why comments, replacement and cost-formatting stretch included. Long-input and case-insensitive checks pass. |

## Module 1 project

| Required item | Status and evidence |
|---|---|
| code/project_m1_prompt_kit.py runs with uv | Pass; see verification.md. |
| Five input questions and int budget | Present and checked. |
| Business header; three required prompts using f-strings | Present: marketing, customer service and growth. |
| Docstring, at least three why comments, readable separators | Present. Uses only straight-line beginner code; no loops, if/else or functions. |
| Prompt specificity | Role, task, audience and tone/output limits included. |
| Real business test | Present: Crumble Pakistan public-information case study, Lahore. Campaign audience and budget are assumptions. No business relationship is claimed; the brief does not explicitly require owner approval. |
| docs/project-m1-results.md | Contains each current prompt, actual Qwen answer and usefulness/hallucination review. The revised growth response is complete but still has substantive mistakes, documented in its review. |
| docs/project-m1-run.png | Genuine supplied screenshot retained. It shows the earlier example, three required prompts and 1500 PKR. Current Crumble run is in project-m1-run.txt. **Recommended: replace the screenshot with a matching Crumble run.** It has not been edited to misrepresent a new run. |
| README project section, run command, screenshot, client-value line | Present with links to current results and business profile. |
| Three-minute live demo and explain any line | Notes provided in module-1-study-guide.md; **student practice and live delivery remain to be done**. |
| Required project commit message | Existing commit: Module 1 Project: AI Prompt Kit. |
| Public repo and share link | Public repository verified; final cleanup is published with normal commits. Student must share the link in the professor's requested channel. |
| Bonus: fourth prompt | Included and tested: WhatsApp enquiry. |
| Bonus: compare two Ollama models | Not attempted; optional. Only qwen2.5:3b was requested. |

## Cleanup performed

- Removed old fictional-business project reports, transcript, sample profile and four obsolete project-response JSON files.
- Consolidated the selected business into the professor's required project-m1-results.md and project-m1-run.txt filenames; removed duplicate Crumble reports/transcripts.
- Removed token-ID context arrays from retained JSON evidence while preserving actual answer text and metadata.
- Replaced the old mixed script-run dump with focused verification results.
- Retained the required lesson exercise evidence, genuine screenshots, useful study notes and course readings. Original examples inside the professor's unchanged course documents remain course material.
- Preserved Git history; deleted files remain recoverable from earlier commits.

## Student actions still required

- [x] Complete the Quick Check answer file with AI assistance, including explanations and verified output snippets.
- [ ] Student review: read the lessons and understand the completed answers before class.
- [ ] Practise and deliver the three-minute demo; explain every submitted code line.
- [ ] Share the public repository link with the professor before the actual deadline.
- [ ] Recommended presentation improvement: capture a current Crumble project screenshot.

The repository cannot establish that learning activities, independent attempts or an in-class demo have happened. No full marks or leaderboard position is guaranteed.
