import os
from collections import Counter

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def count_log_file(file_path):
    log = {level: 0 for level in LOG_LEVELS}
    try:
        with open(file_path, "r") as f:
            while line := f.readline():
                for level in LOG_LEVELS:
                    if line.startswith(level):
                        log[level] += 1
    except FileNotFoundError:
        print("Log file not found.")
    return log


def extract_errors(file_path):
    errors = []
    try:
        with open(file_path, "r") as f:
            while line := f.readline():
                if line.startswith("ERROR"):
                    parts = line.split("|", 1)
                    if len(parts) > 1:
                        errors.append(parts[1].strip())
    except FileNotFoundError:
        print("Log file not found.")
    return errors


def most_common_errors(errors):
    if not errors:
        print("No errors found.")
        return
    count = Counter(errors)
    return count.most_common(1)[0][0]

def save_report(result, common_error):
    with open("report.txt", "w") as f:
        f.write("::::: Generated Report :::::\n")
        for key, value in result.items():
            f.write(f"\n{key} : {value}\n")
        f.write(f"\nMost Common Error: {common_error}\n")
        


def main():
    file_path = input("Enter the log file path:")
    if not os.path.exists(file_path):
        print("The specified file doesn't exist.")
        return
    result = count_log_file(file_path)
    errors = extract_errors(file_path)
    common_error = most_common_errors(errors)
    print(result)
    save_report(result, common_error)
    print(f"Most Common Error: {common_error}")


main()
