import json
import signal
import random
from json import JSONDecodeError

FILE = "data/questions.json"

class TimeoutException(Exception):
    pass

def handler(signum, frame):
    raise TimeoutException

def load_questions():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except JSONDecodeError:
        return []
    
def main():
    questions = load_questions()
    random.shuffle(questions)
    score = 0
    print("::::: Quiz Application :::::")
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

    print(f"You scored {score}/{len(questions)}")

main()
        
