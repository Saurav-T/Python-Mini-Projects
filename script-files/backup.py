import os
import sys
import shutil
from datetime import datetime

IGNORE_DIRS = ["venv", ".git", "__pycache__"]
log = [] 

def append_log(message):
    log.append(message + "\n")

def should_copy(src, dest):
    if not os.path.exists(dest):
        return True
    return os.path.getmtime(src) > os.path.getmtime(dest)

def copy_files(source, backup):
    for root, dirs, filenames in os.walk(source):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        relative_path = os.path.relpath(root, source)
        dest_folder = os.path.join(backup, relative_path)
        os.makedirs(dest_folder, exist_ok=True)

        for file in filenames:
            src = os.path.join(root, file)
            dest = os.path.join(dest_folder, file)

            try:
                if should_copy(src, dest):
                    shutil.copy2(src, dest)
                    append_log(f"{datetime.now()} ::: COPIED ::: {src}")
                else:
                    append_log(f"{datetime.now()} ::: SKIPPED ::: {src}")

            except Exception as e:
                append_log(f"{datetime.now()} ::: ERROR ::: {src} ::: {e}")

def save_log():
    with open("backup.log", "a", encoding="utf-8") as f:
        f.writelines(log)

def main():
    if len(sys.argv) < 3:
        print("Usage: python backup.py <source> <backup>")
        return

    source = os.path.abspath(sys.argv[1])
    backup = os.path.abspath(sys.argv[2])

    if backup.startswith(source):
        print("Error: backup folder cannot be inside source folder")
        return

    if not os.path.exists(source):
        print("Filepath doesn't exist")
        return

    copy_files(source, backup)
    save_log()

    print("Backup completed successfully.")
    print("Log updated.")

if __name__ == "__main__":
    main()