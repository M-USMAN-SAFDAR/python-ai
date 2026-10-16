# Toolkit verification — 16 October 2026

| Tool | Actual version |
|---|---|
| uv | 0.12.13 |
| Project Python | 3.13.15 |
| VS Code | 1.141.2 |
| Git | 2.54.0.windows.1 |
| Ollama | 0.34.0 |
| Claude Code | 2.1.283 |

Ollama's local API lists `qwen2.5:3b`, Q4_K_M, with model context capacity 32768. No second model was downloaded for bonus comparison.

Claude is installed at `C:\Users\usman\.local\bin\claude.exe` but was not found by the current terminal PATH. Its version command works using that full path. Account login and paid access were not tested.

VS Code's version command printed a sandbox chdir error followed by its version. Version 1.141.2 was independently confirmed in the installed application's package.json.

Run the following from the project folder in PowerShell and save a genuine screenshot as `docs/setup-check.png`:

```powershell
uv --version
uv run python --version
code --version
git --version
ollama --version
& "$env:USERPROFILE\.local\bin\claude.exe" --version
```

A genuine student-supplied screenshot is saved as [setup-check.png](setup-check.png). It shows all six version commands succeeding in Command Prompt. The PowerShell commands above are an alternative way to reproduce the checks.
