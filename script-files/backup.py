import os
import sys
import shutil
import json
import hashlib
from datetime import datetime
from json import JSONDecodeError

IGNORE_DIRS = ["venv", ".git", "__pycache__"]
METADATA_FILE = "metadata.json"

log = [] 

def append_log(message):
    log.append(message + "\n")

def load_metadata():
    try:
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    except (JSONDecodeError, FileNotFoundError):
        return {}
    
def save_metadata(data):
    with open(METADATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print("Metadata saved successfully.")

def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
        
    return hasher.hexdigest()   

def should_copy(src, dest):
    if not os.path.exists(dest):
        return True
    return get_file_hash(src) != get_file_hash(dest)

def copy_files(source, backup, metadata):
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
                    metadata[os.path.relpath(src, source)] = {
                        "hash": get_file_hash(src),
                        "last_modified": os.path.getmtime(src),
                        "backup_path": dest
                    }
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

    metadata = load_metadata()
    source = os.path.abspath(sys.argv[1])
    backup = os.path.abspath(sys.argv[2])

    if backup.startswith(source):
        print("Error: backup folder cannot be inside source folder")
        return

    if not os.path.exists(source):
        print("Filepath doesn't exist")
        return

    copy_files(source, backup, metadata)
    save_log()
    save_metadata(metadata)
    
    print("Backup completed successfully.")
    print("Log updated.")

if __name__ == "__main__":
    main()



