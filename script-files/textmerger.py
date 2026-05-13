import os
import sys 


def get_files_by_extension(folder, extension):
    files = []
    IGNORE_DIRS = ["__pycache__", "venv", ".git", "expvenv"]
    for root, dirs, filenames in os.walk(folder):
        dirs[:] = [f for f in dirs if f not in IGNORE_DIRS]
        for file in filenames:
            if os.path.splitext(file)[1].lower() == extension.lower():
                files.append(os.path.join(root, file))

    return files

def read_file_content(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            return content
    except (FileNotFoundError, UnicodeDecodeError, PermissionError):
        print(f"Failed to read file: {file_path}")

def composer(files):
    output = ""

    for file in files:
        content = read_file_content(file)
        output += f"\n\n===== {os.path.relpath(file)} =====\n\n"
        output += content if content else ""

    return output

def write_output(data, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)

def main():
    if len(sys.argv) < 3:
        print("Usage: python textmerger.py <folder-path> <extension> [output-file]")
        return
    path = sys.argv[1]
    if not os.path.exists(path):
        print("Path Not Found.")
        return
    extension = sys.argv[2]
    location = sys.argv[3] if len(sys.argv) > 3 else "output.txt"
    files = get_files_by_extension(path, extension)
    if not files:
        print("No matching files found")
        return
    data = composer(files)
    write_output(data, location)

main()

