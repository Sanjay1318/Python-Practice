# Function to safely take marks between 0 and 100
def get_marks(subject):
    while True:
        marks = float(input(f"Enter Your Marks in {subject} : "))

        # Check valid range
        if 0 <= marks <= 100:
            return marks
        else:
            print(" Invalid Marks! Enter marks value between 0 and 100 only.")

# ---- Taking Valid Input ----
marks1 = get_marks("Mathematics")
marks2 = get_marks("Physics")
marks3 = get_marks("Chemistry")
marks4 = get_marks("Biology")
marks5 = get_marks("Computer Applications")

# Store subjects and marks together using dictionary
# Key = Subject Name
# Value = Marks
subjects = {
    "Mathematics": marks1,
    "Physics": marks2,
    "Chemistry": marks3,
    "Biology": marks4,
    "Computer Applications": marks5
}

# ---- Average Calculation ----
# sum() adds all marks
# len() gives number of subjects
marks_average = sum(subjects.values()) / len(subjects)

# ---- Finding Highest and Lowest Marks ----
# max(dictionary, key=dictionary.get) → gives key having highest value
highest_marks = max(subjects.values())
lowest_marks = min(subjects.values())

# Get all subjects having highest marks
highest_subjects = [sub for sub, mark in subjects.items() if mark == highest_marks]

# Get all subjects having lowest marks
lowest_subjects = [sub for sub, mark in subjects.items() if mark == lowest_marks]

print("\n------ RESULT ------")
print("Average Marks :", marks_average)

print("Highest Marks :", highest_marks)
print("Subjects with Highest Marks:")
for s in highest_subjects:
    print("→", s)

print("\nLowest Marks :", lowest_marks)
print("Subjects with Lowest Marks:")
for s in lowest_subjects:
    print("→", s)

# ---- Grade System Based on Average ----
# Checking average and assigning grade
if marks_average >= 90:
    grade = "A+"
elif marks_average >= 80:
    grade = "A"
elif marks_average >= 70:
    grade = "B"
elif marks_average >= 60:
    grade = "C"
elif marks_average >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\nGrade :", grade)
