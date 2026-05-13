import sys
import os

IGNORE_DIRS = ["venv", ".git", "__pycache__"]
TEXT_EXTENSIONS = {
    ".py", ".txt", ".md", ".json", ".csv", ".html", ".css", ".js"
}


def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            content = f.read()
            return content
    except (FileNotFoundError, PermissionError, UnicodeDecodeError):
        print(f"Failed to read file: {file_path}")
        return ""


def get_files(path, search):
    output = []
    for root, dirs, filenames in os.walk(path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in filenames:
            ext = os.path.splitext(file)[1].lower()
            if ext not in TEXT_EXTENSIONS:
                continue
            file_path = os.path.join(root, file)
            content = read_file_content(file_path)
            if search in content:
                output.append(file_path)

    return output


def main():
    if len(sys.argv) < 3:
        print("Usage: python file-searcher.py <folder-path> <search-text>")
        return
    path = sys.argv[1]
    search = sys.argv[2]

    if not os.path.exists(path):
        print("Filepath doesn't exist")
        return

    results = get_files(path, search)
    print("\nMatching Files:\n")
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
