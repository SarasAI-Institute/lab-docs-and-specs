"""Create disposable organizer inputs or check them against their original snapshot."""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1] / 'sandbox'

def snapshot(folder):
    result = {}
    for path in sorted(folder.rglob('*')):
        key = path.relative_to(folder).as_posix()
        if path.is_symlink():
            result[key] = 'symlink:' + str(path.readlink())
        elif path.is_dir():
            result[key] = 'directory'
        elif path.is_file():
            result[key] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result

def create():
    ROOT.mkdir(exist_ok=True)
    folder = Path(tempfile.mkdtemp(prefix='practice-', dir=ROOT))
    samples = {
        'notes.txt': 'Practice notes.\n',
        'photo.PNG': 'Text-only stand-in; this exercise classifies extensions.\n',
        'bundle.zip': 'Text-only stand-in; not an actual archive.\n',
        'script.py': 'print("practice")\n',
        'mystery.xyz': 'Unknown extension.\n',
        'documents/notes.txt': 'Existing destination; never overwrite.\n',
        'nested/leave-me.txt': 'Nested file; leave untouched.\n',
    }
    for relative, content in samples.items():
        path = folder / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
    baseline = ROOT / (folder.name + '.json')
    baseline.write_text(json.dumps(snapshot(folder), indent=2), encoding='utf-8')
    print(folder.relative_to(ROOT.parent).as_posix())
    print('Fresh disposable folder created; its baseline is stored beside it.')

def verify(value):
    folder = Path(value)
    if folder.is_symlink() or not folder.is_dir() or folder.resolve().parent != ROOT.resolve():
        raise SystemExit('Choose a generated practice folder directly inside sandbox/.')
    baseline = ROOT / (folder.name + '.json')
    if not baseline.is_file():
        raise SystemExit('No original snapshot exists for this folder.')
    before = json.loads(baseline.read_text(encoding='utf-8'))
    after = snapshot(folder)
    changes = [key for key in sorted(before.keys() | after.keys()) if before.get(key) != after.get(key)]
    if changes:
        print('CHANGED: ' + ', '.join(changes))
        raise SystemExit(1)
    print('UNCHANGED: file paths, contents and directory structure match the original snapshot.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('create')
    check = sub.add_parser('verify')
    check.add_argument('folder')
    args = parser.parse_args()
    if args.command == 'create':
        create()
    else:
        verify(args.folder)
