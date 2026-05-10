import json
import signal
import random
from json import JSONDecodeError

FILE = "data/questions.json"
LEADERBOARD_FILE = "data/leaderboard.json"

class TimeoutException(Exception):
    pass

def handler(signum, frame):
    raise TimeoutException

def load_questions():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (JSONDecodeError, FileNotFoundError):
        return []
    
def save_score(name, score, total):
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            data = json.load(f)
    except (JSONDecodeError, FileNotFoundError):
        data = []

    data.append({
        "name" : name,
        "score" : score,
        "total" : total
    })

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            entry = json.load(f)
        
        entry.sort(key=lambda x:x["score"], reverse=True)

        print("===== Leaderboard =====")
        for i, entry in enumerate(entry, start=1):
            print(f"{i}. {entry['name']}: {entry['score']}/{entry['total']}")
            
    except (JSONDecodeError, FileNotFoundError):
        print("No leaderboard data yet")

    

def main():
    questions = load_questions()
    random.shuffle(questions)
    score = 0
    print("::::: Quiz Application :::::")
    name = input("Enter your name:")
    print("Choose option a, b, c or d.")
    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q["question"]}")
        options = q["options"]
        for key, value in options.items():
            print(f"{key}. {value}")

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(5)
        print("You have 5 seconds to answer.")
        try:
            answer = input("Answer: ")[0]
            if q["answer"].lower() == answer.lower():
                score += 1
        except TimeoutException:
            print("Time's Up")
    total = len(questions)
    print(f"You scored {score}/{total}")
    save_score(name, score, total)
    show_leaderboard()
    

main()
        
