import json
from json import JSONDecodeError

FILE = "data/questions.json"

def load_questions():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except JSONDecodeError:
        return []
    
def main():
    questions = load_questions()
    score = 0
    print("::::: Quiz Application :::::")
    print("Choose option a, b, c or d.")
    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q["question"]}")
        options = q["options"]
        for key, value in options.items():
            print(f"{key}. {value}")
        answer = input("Answer: ")[0]
        if q["answer"].lower() == answer.lower():
            score += 1

    print(f"You scored {score}/{len(questions)}")

main()
        
