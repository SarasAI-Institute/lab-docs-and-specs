import argparse
import shutil
from pathlib import Path

EXTENSION_MAP = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'archives': ['.zip', '.tar', '.gz', '.rar'],
    'code': ['.py', '.js', '.html', '.css', '.java']
}

def get_category(extension):
    for category, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return category
    return 'others'

def move_file(file_path, base_dir):
    category = get_category(file_path.suffix)
    dest_dir = base_dir / category
    if dest_dir.is_symlink():
        print(f'Skipping {file_path.name}: category directory is a symbolic link')
        return
    dest_dir.mkdir(exist_ok=True)
    dest_path = dest_dir / file_path.name
    if dest_path.exists() or dest_path.is_symlink():
        print(f'Skipping {file_path.name}: already exists')
        return
    shutil.move(str(file_path), str(dest_path))
    print(f'Moved {file_path.name} to {category}/')

def organize_directory(path):
    base_dir = Path(path)
    if base_dir.is_symlink() or not base_dir.is_dir():
        raise ValueError('Choose an existing directory that is not a symbolic link')
    script_path = Path(__file__).resolve()
    for item in sorted(base_dir.iterdir()):
        if item.is_symlink():
            continue
        if item.is_file() and item.resolve() != script_path:
            move_file(item, base_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organize top-level files by extension.')
    parser.add_argument('directory')
    args = parser.parse_args()
    try:
        organize_directory(args.directory)
    except (ValueError, OSError) as exc:
        parser.exit(2, f'Error: {exc}\n')
