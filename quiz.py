# Initialize the score variable (Type Integrity)
score = 0

print("Welcome to the General Knowledge Quiz!\n")

# Question 1
answer1 = input("1. What is the capital of France? ").strip().lower()
if answer1 == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Paris.\n")

# Question 2
answer2 = input("2. Which planet is known as the Red Planet? ").strip().lower()
if answer2 == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Mars.\n")

# Question 3
answer3 = input("3. What is 5 + 7? ").strip().lower()
if answer3 == "12":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 12.\n")

# Final Output using an f-string
print(f"Quiz Complete! Your final score is {score}/3.")