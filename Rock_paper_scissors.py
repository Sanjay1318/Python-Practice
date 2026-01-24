import random

print("Welcome to Rock Paper Scissors")

user_choice = input("Enter rock / paper / scissors : ").lower()
computer_choice = random.choice(["rock","paper","scissors"])

print("You chose :", user_choice)
print("Computer chose :", computer_choice)

if user_choice == computer_choice:
    print("It's a Draw!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You Won ")
elif user_choice == "paper" and computer_choice == "rock":
    print("You Won ")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You Won ")
else:
    print("Computer Wins")
