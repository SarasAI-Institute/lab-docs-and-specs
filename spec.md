# Dry-run feature — my specification

Complete this document and commit it before implementing the feature. The constraints below are the lab contract; fill in the reasoning, examples and plan yourself.

## Goal and user story

Who needs this feature, and why?

## Required behavior

- Keep the existing positional directory argument; add the optional `--dry-run` flag.
- Dry run reports the same eligible top-level moves as normal mode, with a clear `[DRY RUN]` prefix and source/destination paths.
- Dry run must not move, create, overwrite or delete files or directories, or change file contents. Reading files can affect filesystem access times; that is outside this lab's comparison.
- Existing destination names are skipped without overwriting, in both modes.
- Existing source directories are not traversed; symbolic-link entries and the script itself remain excluded. A destination category that is a symbolic link is skipped.
- Missing, file-valued or symbolic-link roots fail clearly with nonzero exit status. Unknown command flags fail before organizing anything.
- Normal mode keeps the existing categories, case-insensitive extension mapping and unknown-extension fallback.
- Output order is stable. The tool assumes a stable local practice folder; concurrent file changes are outside scope.

## Acceptance examples

| Input / starting state | Command | Expected output meaning | Filesystem result |
|---|---|---|---|
| | | | |

Include a new destination directory, an existing filename collision, nested files, an unknown extension, mixed-case extensions, an empty folder and invalid input.

## Decisions and plan

How will normal and preview modes use the same planned destinations? What constitutes a skipped file? How will failures be reported? List small implementation steps and how each will be checked.

## Evidence

- Specification commit:
- Implementation commits:
- Actual verification commands/results:
- Any specification changes and why:
