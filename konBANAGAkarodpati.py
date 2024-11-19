import random

# Questions and their respective answers
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest mammal?": "Blue Whale",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare"
}

def ask_question():
    """Ask a random question from the dictionary"""
    question = random.choice(list(questions.keys()))
    correct_answer = questions[question]
    user_answer = input(question + "\nYour answer: ").strip()
    return user_answer.lower() == correct_answer.lower()

def main():
    print("Welcome to Kaun Banega Crorepati!\n")
    score = 0
    for _ in range(5):  # Ask 5 questions
        if ask_question():
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
    
    print(f"Quiz finished! You scored {score}/5.")

if __name__ == "__main__":
    main()
                         