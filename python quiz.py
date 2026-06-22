# Cybersecurity Quiz App

questions = [
    {
        "question": "What does HTTPS stand for?",
        "options": [
            "Hyper Text Transfer Protocol Secure",
            "High Transfer Text Protocol System",
            "Hyper Tool Transfer Protocol Service",
            "None of the above"
        ],
        "answer": 1
    },
    {
        "question": "Which of the following is a strong password?",
        "options": [
            "123456",
            "password",
            "Cyber@12345",
            "qwerty"
        ],
        "answer": 3
    },
    {
        "question": "What is phishing?",
        "options": [
            "A type of fishing",
            "A cyber attack to steal information",
            "A programming language",
            "A firewall"
        ],
        "answer": 2
    },
    {
        "question": "Which software helps protect a computer from malware?",
        "options": [
            "Antivirus",
            "Calculator",
            "Paint",
            "Notepad"
        ],
        "answer": 1
    },
    {
        "question": "What should you do before clicking a suspicious link?",
        "options": [
            "Click immediately",
            "Ignore security warnings",
            "Verify the source",
            "Share it with friends"
        ],
        "answer": 3
    }
]

score = 0

print("===== Cybersecurity Quiz =====\n")

for i, q in enumerate(questions, start=1):
    print(f"Q{i}. {q['question']}")

    for j, option in enumerate(q["options"], start=1):
        print(f"{j}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print("===== Quiz Finished =====")
print(f"Your Score: {score}/{len(questions)}")

if score == len(questions):
    print("Excellent! Cybersecurity Expert!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Learning Cybersecurity!")