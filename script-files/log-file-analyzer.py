import os
from collections import Counter

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def analyze_log(file_path):
    counts = {level: 0 for level in LOG_LEVELS}
    errors = []

    try:
        with open(file_path, "r") as f:
            while line := f.readline():
                data = parse_log_line(line)
                level = data["level"]

                if level in counts:
                    counts[level] += 1

                if level == "ERROR":
                    errors.append(data["message"])

    except FileNotFoundError:
        print("Log file not found.")

    return counts, errors


def most_common_errors(errors):
    if not errors:
        print("No errors found.")
        return None
    return Counter(errors).most_common(1)[0][0]

def save_report(result, common_error):
    with open("report.txt", "w") as f:
        f.write("::::: Generated Report :::::\n")
        for key, value in result.items():
            f.write(f"\n{key} : {value}\n")
        f.write(f"\nMost Common Error: {common_error}\n")
        
def parse_log_line(line):
    if " | " in line:
        parts = line.split(" | ", 2)
        if len(parts) == 3:
            return {
                "timestamp": parts[0].strip(),
                "level": parts[1].strip(),
                "message": parts[2].strip()
            }
        
    elif ":" in line:
        level, message = line.split(":", 1)
        return {
            "timestamp": None,
            "level": level.strip(),
            "message": message.strip()
        }
        
    return {
        "timestamp": None,
        "level": "UNKNOWN",
        "message": line.strip()
    }

def main():
    file_path = input("Enter the log file path:")
    if not os.path.exists(file_path):
        print("The specified file doesn't exist.")
        return
    result, errors = analyze_log(file_path)
    common_error = most_common_errors(errors)
    print(result)
    print(f"Most Common Error: {common_error}")
    save_report(result, common_error)

main()
