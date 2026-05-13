import os
import sys
import shutil

def copy_files(source, backup):
    for root, dirs, filenames in os.walk(source):
        relative_path = os.path.relpath(root, source)
        dest_folder = os.path.join(backup, relative_path)
        os.makedirs(dest_folder, exist_ok=True)
        for file in filenames:
            src = os.path.join(root, file)
            dest = os.path.join(dest_folder, file)
            shutil.copy2(src, dest)


def main():
    if len(sys.argv) < 3:
        print("Usage: python backup.py <source-folder> <backup-folder>")
        return
    source = sys.argv[1]
    backup = sys.argv[2]
    if not os.path.exists(source):
        print("Filepath doesn't exist")
        return
    
    copy_files(source, backup)
    print("Backup completed sucessfully.")
    
main()
