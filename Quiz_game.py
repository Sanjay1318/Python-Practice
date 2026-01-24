import random   # Used if you want to shuffle questions later

print(" Welcome to the Quiz Game!")

# Showing user difficulty options
print("Choose Difficulty Level")
print("1. Easy")
print("2. Medium")
print("3. Hard")

# Taking user level choice
choice = int(input("Enter your choice (1/2/3): "))
score = 0   # To store correct answers

# ---------------- EASY QUESTIONS ----------------
# Format: ["Question", ["Option1","Option2","Option3","Option4"], correct_option_index] # index starts from 0(zero) so option 1 index is 0 and so on
easy_questions = [
    ["What is the capital of India?", ["Delhi","Mumbai","Hyderabad","Kolkata"], 0],
    ["How many days are there in a week?", ["5","6","7","8"], 2],
    ["What is the national animal of India?", ["Lion","Tiger","Elephant","Deer"], 1],
    ["What is 2 + 2?", ["3","4","5","6"], 1],
    ["Which planet is known as Red Planet?", ["Earth","Mars","Jupiter","Venus"], 1],
    ["What is the capital of USA?", ["New York","Los Angeles","Washington DC","Chicago"], 2],
    ["How many letters in English alphabet?", ["24","26","28","30"], 1],
    ["Sun rises in the?", ["West","East","North","South"], 1],
    ["Which is the largest ocean?", ["Indian","Pacific","Atlantic","Arctic"], 1],
    ["Which is the smallest continent?", ["Asia","Europe","Australia","Africa"], 2]
]

# ---------------- MEDIUM QUESTIONS ----------------
medium_questions = [
    ["Who invented the telephone?",["Edison","Graham Bell","Newton","Tesla"],1],
    ["Which gas do plants absorb?",["Oxygen","Carbon Dioxide","Nitrogen","Helium"],1],
    ["What is H2O?",["Salt","Hydrogen","Water","Acid"],2],
    ["Who wrote Ramayana?",["Valmiki","Tulsidas","Vyasa","Kalidas"],0],
    ["Which is largest desert?",["Gobi","Thar","Sahara","Kalahari"],2],
    ["Which one is programming language?",["Python","HTML","CSS","XML"],0],
    ["Fastest land animal?",["Cheetah","Tiger","Horse","Lion"],0],
    ["Where is Taj Mahal?",["Delhi","Agra","Mumbai","Jaipur"],1],
    ["Human body has how many bones?",["206","201","300","108"],0],
    ["Largest mammal?",["Elephant","Blue Whale","Shark","Giraffe"],1]
]

# ---------------- HARD QUESTIONS ----------------
hard_questions = [
    ["Who discovered gravity?",["Einstein","Newton","Tesla","Galileo"],1],
    ["Which is longest river?",["Nile","Amazon","Ganga","Yangtze"],0],
    ["Who wrote Hamlet?",["Milton","Wordsworth","Shakespeare","Keats"],2],
    ["Light travels at?",["3x10^8 m/s","3x10^6 m/s","1x10^8 m/s","9x10^8 m/s"],0],
    ["Largest planet?",["Earth","Mars","Jupiter","Saturn"],2],
    ["Who painted Mona Lisa?",["Picasso","Da Vinci","Michelangelo","Rafael"],1],
    ["Gold chemical symbol?",["Au","Ag","Go","Gd"],0],
    ["Where is Great Wall?",["India","China","Japan","Russia"],1],
    ["Smallest bone in body?",["Stapes","Femur","Ribs","Ulna"],0],
    ["Brain of computer?",["RAM","CPU","ROM","GPU"],1]
]

# ---------------- SELECTING LEVEL ----------------
# Based on user input, we assign the respective question list
if choice == 1:
    questions = easy_questions
    print("\n EASY LEVEL SELECTED\n")
elif choice == 2:
    questions = medium_questions
    print("\n MEDIUM LEVEL SELECTED\n")
else:
    questions = hard_questions
    print("\n HARD LEVEL SELECTED\n")

# If you want random order, uncomment:
# random.shuffle(questions)

qno = 1   # Question number counter

# Loop through each question one by one
for q in questions:
    print(f"Q{qno}. {q[0]}")      # Printing question
    # Printing options with numbering
    for i, option in enumerate(q[1]):
        print(f"{i+1}. {option}")

    # Taking user's answer
    answer = int(input("Enter your answer (1/2/3/4): "))

    # Checking if user answer matches correct option
    if answer-1 == q[2]:
        print("Correct ")
        score += 1   # Increase score
    else:
        print("Wrong ")

    print("------------------------")
    qno += 1  # Move to next question

# ---------------- RESULT SECTION ----------------
print(f" Your Final Score: {score} / 10")
