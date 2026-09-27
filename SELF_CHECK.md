# Documentation and Specs self-check

Generate fresh data with `python tools/sandbox.py create`. Use the printed path as `YOUR_FOLDER`.

## Preview changes without making them

After you implement the feature:

```sh
python file_organizer.py YOUR_FOLDER --dry-run
python tools/sandbox.py verify YOUR_FOLDER
```

The second command must report UNCHANGED and exit successfully. Preview output should report eligible moves to images, archives, code and others. The root notes.txt must be skipped because documents/notes.txt already exists. The nested folder remains untouched. The snapshot tool checks paths, bytes and directories, not console wording or whether the planned categories are correct: inspect those separately.

On the initial starter, `--dry-run` is rejected. That rejection is not a successful implementation of preview mode.

## Check normal mode

Run normal mode on a fresh practice folder. Confirm photo.PNG goes to images, bundle.zip to archives, script.py to code and mystery.xyz to others. Both notes.txt files retain their original bytes and locations, and nested/leave-me.txt stays put. A second normal run should skip the remaining collision without duplicating or overwriting files. The snapshot tool should now report CHANGED; that is expected after real organization.

## Check boundaries and documentation

- An empty practice directory succeeds without unnecessary output or moves.
- Missing or file-valued roots fail clearly; unknown flags cause no changes.
- If your platform permits creating test symlinks, verify exclusions using only disposable fixtures; do not require administrator access just for this optional check.
- PROJECT_DOCS.md and docstrings describe actual behavior, limitations and return/error behavior accurately.
- The spec was committed before implementation.
- Project instructions are relevant, and the recorded before/after comparison is real.

If a check fails, identify one difference between the expected and observed behavior before requesting another edit.
