"""
import random

random_number = random.randint(1,100)
attempts = 0
user_number = 0

while user_number != random_number:
    user_number = int(input("Guess Number : "))
    attempts += 1

    if user_number > random_number:
        print("Greater")
    elif user_number < random_number:
        print("Smaller")
    else:
        print("Correct Guess")
"""
        
        # OR
"""
import random

print("Welcome to the Number Guessing Game")
print("------------------------------------")
print("Choose Difficulty Level : ")
print("1. Easy (1 - 20)")
print("2. Medium (1 - 20)")
print("3. Hard (1 - 20)")

choice = int(input("Enter your Choice (1/2/3) : "))

if choice == 1:
    number = random.randint(1,20)
    chances = 10
    print("\n EASY MODE SELECTED (1 - 20)\n")
elif choice == 2:
    number = random.randint(1,50)
    chances = 8
    print("\n MEDIUM MODE SELECTED (1 - 50)\n")
else:
    number = random.randint(1,100)
    chances = 5
    print("\n Hard MODE SELECTED (1 - 100)\n")

attempts = 0

while chances > 0:
    guess = int(input(" Enter your guess: "))
    attempts += 1
    chances -= 1

    if guess == number:
        print(f"\n CORRECT! You guessed it in {attempts} attempts!")
        break
    elif guess > number:
        print(" Too High! Try something smaller.")
    else:
        print(" Too Low! Try something bigger.")

    print(f" Attempts left: {chances}\n")

if chances == 0 and guess != number:
    print("\n Out of chances!")
    print(" The correct number was: {number}")

print(f"\nThanks for playing")
"""