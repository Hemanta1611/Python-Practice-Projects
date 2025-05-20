def main():
    print("Hello, World!")

import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ["Berlin", "Paris", "Madrid", "Rome"],
        "answer": "Berlin"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["Rome", "Paris", "Madrid", "Berlin"],
        "answer": "Rome"
    },
    {
        "question": "What is the capital of Spain?",
        "options": ["Madrid", "Paris", "Rome", "Berlin"],
        "answer": "Madrid"
    },
    {
        "question": "What is the capital of Portugal?",
        "options": ["Lisbon", "Paris", "Rome", "Berlin"],
        "answer": "Lisbon"
    },
    {
        "question": "What is the capital of Greece?",
        "options": ["Athens", "Paris", "Rome", "Berlin"],
        "answer": "Athens"
    },
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Paris", "Rome", "Berlin"],
        "answer": "New Delhi"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Tokyo", "Paris", "Rome", "Berlin"],
        "answer": "Tokyo"
    }
]

def game():
    score = 0
    # randomly select 5 questions from the list
    selected_questions = random.sample(questions, 5)

    for question in selected_questions:
        print("Q. ", question["question"])
        print("Options: ", question["options"])
        ans = input("Enter your answer: ")
        
        if ans == question["answer"]:
            print("Correct answer \n")
            score+=1
        else:
            print("Wrong answer")
            print("Correct answer is: ", question["answer"], "\n")
                
    
    return score

total_score = game()
print("Total Score: ", total_score, "/5")

# if __name__ == "__main__":
#     main()