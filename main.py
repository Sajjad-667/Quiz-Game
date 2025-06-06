#### Quiz Game 

# Simple Quiz Game using if-else and for loop

score = 0

# Dictionary with questions and their correct answers
questions = {
    "What is the capital of France? ": "paris",
    "What is 5 + 7? ": "12",
    "What color is the sky on a clear day? ": "blue"
}

# Loop through each question and get user input
for question, correct_answer in questions.items():
    answer = input(question).strip().lower()
    if answer == correct_answer:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect!")

# Print the final score
print(f"\nYour final score: {score} / {len(questions)}")