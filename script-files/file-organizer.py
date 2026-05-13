import os
import shutil

FILE_TYPES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.docx', '.txt'],
    'spreadsheets': ['.xlsx', '.csv'],
    'presentations': ['.pptx'],
    'videos': ['.mp4', '.mkv', '.mov'],
    'audios': ['.mp3', '.wav'],
    'archives': ['.zip', '.rar', '.tar.gz']
}

def get_files(folder):
    return [ f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
        
    return "Others"

def organize(folder):
    folder = os.path.expanduser(folder)
    files = get_files(folder)

    for file in files:
        src = os.path.join(folder, file)
        category = get_category(file)

        dest_folder = os.path.join(folder, category)
        os.makedirs(dest_folder, exist_ok=  True)

        dest = os.path.join(dest_folder, file)
        shutil.move(src, dest) 

    print("Files organized successfully!")


if __name__ == "__main__":
    path = input("Enter folder path: ")
    organize(path)