def quizGame():
    questions = [
        {"question": "What is the capital of France?", "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"], "correctAnswer": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "correctAnswer": "B"},
        {"question": "What is the largest mammal in the world?", "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Gorilla"], "correctAnswer": "B"}
    ]

    score = 0

    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        
        userAnswer = input("Enter the letter of your answer (A, B, C, or D): ").upper()

        if userAnswer == question["correctAnswer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is {question['correctAnswer']}.\n")

    print(f"You scored {score}/{len(questions)}.")

quizGame()