import os
import sys
import shutil

IGNORE_DIRS = ["venv", ".git", "__pycache__"]
def copy_files(source, backup):
    for root, dirs, filenames in os.walk(source):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        relative_path = os.path.relpath(root, source)
        dest_folder = os.path.join(backup, relative_path)
        os.makedirs(dest_folder, exist_ok=True)
        for file in filenames:
            src = os.path.join(root, file)
            dest = os.path.join(dest_folder, file)
            if should_copy(src, dest):
                try:
                    shutil.copy2(src, dest)
                except Exception as e:
                    print(f"Skipping {src}: {e}")
            else:
                print(f"Skipped (unchanged): {src}")

def should_copy(src, dest):
    if not os.path.exists(dest):
        return True
    
    return os.path.getmtime(src) > os.path.getmtime(dest)

def main():
    if len(sys.argv) < 3:
        print("Usage: python backup.py <source-folder> <backup-folder>")
        return
    source = sys.argv[1]
    backup = sys.argv[2]

    source = os.path.abspath(source)
    backup = os.path.abspath(backup)

    if backup.startswith(source):
        print("Error: backup folder cannot be inside source folder")
        return

    if not os.path.exists(source):
        print("Filepath doesn't exist")
        return
    
    copy_files(source, backup)
    print("Backup completed sucessfully.")
    
main()
