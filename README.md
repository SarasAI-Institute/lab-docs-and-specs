# Module 3 mini-lab — Documentation and Specs

Turn an unfamiliar file organizer into a documented tool, then specify and implement a small dry-run feature. Practice documenting facts, writing testable requirements and giving your coding assistant useful project instructions.

## Your starting point

`file_organizer.py` is a working, lightly documented script. It **moves files**. Dry run is not implemented: passing `--dry-run` currently produces an argument error before moving anything. Your assignment is to document the existing behavior and add the feature from your own committed specification.

The starter already rejects invalid roots and excludes its own file and symbolic-link entries. These remove distractions from the documentation task. No third-party Python packages are needed.

## Local setup

Download **Code → Download ZIP** from this repository and extract it into a new folder, or clone it if you already use Git. Open that folder in your editor. Use Python 3.12 and Git, with the Codex or Claude Code setup you established in Module 1. No Codespaces, devcontainer or shared API key is needed.

From the lab folder, create and activate a virtual environment:

| Platform | Create | Activate |
|---|---|---|
| macOS / Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |
| Windows PowerShell | `py -3.12 -m venv .venv` | `.venv\Scripts\Activate.ps1` |

All subsequent Python commands use `python` in that active environment. If you downloaded a ZIP, initialize a local Git repository and commit the supplied starter before working. If you cloned it, retain the starter commit. Commit small changes as you go.

## Use disposable practice data

Run this from the lab root:

```sh
python tools/sandbox.py create
```

The first output line is a fresh folder such as `sandbox/practice-abcd1234`. Copy your actual generated path wherever the examples below show `YOUR_FOLDER`. The files are harmless text stand-ins; classification depends on their extensions.

```sh
python file_organizer.py YOUR_FOLDER
```

This command really moves the sample files. Use only the generated practice folder for this lab. Each `create` command gives you a fresh folder; no reset deletes your earlier work. Do not point the organizer at the repository root, Downloads or your personal files.

## Tasks

1. **Investigate.** Read all three functions and the command entry point. Predict what will happen to each fixture, including duplicate destination names and nested files. Run against a disposable folder and compare the result.
2. **Document reality.** Write PROJECT_DOCS.md with setup, usage, supported categories, collision policy, scope and limitations. Add accurate Google-style function docstrings. Keep future dry-run behavior out of the current usage section until implemented.
3. **Guide the assistant.** Write a short project-specific AGENTS.md or CLAUDE.md for your chosen tool. Include relevant constraints such as preserving files on collisions and working only with disposable data. Compare one actual output before and after the instructions; record what changed.
4. **Specify first.** Complete [spec.md](spec.md) with stories, exact behavior, acceptance examples and an implementation plan. Commit the specification before changing the organizer to support dry run.
5. **Implement and verify.** Add `--dry-run` with your assistant, inspect the diff and run your self-checks. Update the usage docs to match the now-implemented feature.

Useful first prompt: “Explain what this script currently does with top-level files, directories and existing destinations. Support each claim with the source. Separate current behavior from the proposed dry-run feature.”

## Finish

Follow [SELF_CHECK.md](SELF_CHECK.md). Demonstrate that dry run leaves file names, bytes and directory structure unchanged, and that normal mode still organizes the fixtures correctly.

## Working with your coding assistant

Use either taught tool; this lab does not require two independent builds. Read the task yourself, supply relevant context, ask for one bounded step, inspect the diff and verify the result. Record a few real decisions in [REFLECTION.md](REFLECTION.md). Try an explanation or hypothesis before requesting implementation. Prompt examples are starting points to adapt, not answers to paste blindly.

This is **ungraded practice**. Keep your work and reflection; there is no submission, mandatory time limit or capstone credit. Apply the method separately to your ongoing PromptLab project. A working mini-lab does not replace capstone evidence.
