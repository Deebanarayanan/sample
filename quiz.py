questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "define", "fun"],
        "answer": "B",
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["int", "str", "bool", "list"],
        "answer": "C",
    },
    {
        "question": "Which method converts a string to lowercase?",
        "options": ["lower()", "small()", "case()", "down()"],
        "answer": "A",
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["list", "tuple", "set", "dictionary"],
        "answer": "D",
    },
    {
        "question": "Which loop is commonly used to iterate over a list?",
        "options": ["for", "define", "switch", "case"],
        "answer": "A",
    }
]
def run_quiz():
    score = 0
    total_questions = len(questions)

    print("="*30)
    print("   PYTHON QUIZ GAME")
    print("="*30)
    print(f"You have {total_questions} questions.")
    print("Select options A, B, C, or D as an answer.")

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {question['question']}")

        for index, option in enumerate(question["options"]):
            letter = chr(ord("A") + index)
            print(f"{letter}. {option}")

        valid_answers = [
            chr(ord("A") + index)
            for index in range(len(question["options"]))
        ]

        while True:
            answer = input("Your answer: ").strip().upper()

            if answer in valid_answers:
                break

            print("Invalid choice. Please enter option A-D Only.")

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print(f"Correct answer: {question['answer']}")
        percentage = score / total_questions * 100

    print("="*20)
    print("           QUIZ RESULTS")
    print("="*20)
    print(f"Correct answers: {score}/{total_questions}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Excellent! You got every question right.")
    elif percentage >= 60:
        print("Good work! Keep practising.")
    else:
        print("Keep learning and try again!")

def main():
    play_again = "yes"
    while play_again.lower() == "yes":
        run_quiz()
        play_again = input("Do you want to retake the quiz? (yes/no): ")
if __name__ == "__main__":
    main()