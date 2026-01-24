"""
print("Welcome to calculator application. Below are the operations available ")
print("1 . Addition ")
print("2 . Subtraction ")
print("3 . Division ")
print("4 . Multiplication ")

choice = int(input("Enter the operation you want to perform (1/2/3/4) :"))

result = 0

if choice < 1 or choice > 4:
    print("Select a valid choice")
else:
    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number : "))

    if choice == 1:
        result = num1 + num2
        print("Addition Result is : ", result)
    elif choice == 2:
        result = num1 - num2
        print("Subtraction Result is : ", result)
    elif choice == 3:
        if num2 == 0:
            print("Error! Division by zero not allowed.")
        else:
            result = num1 / num2
            print("Division Result is : ", result)
    else:
        result = num1 * num2
        print("Multiplication Result is : ", result)
"""
                # OR

while True:

    print("\nWelcome to Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you for using calculator ")
        break

    if choice < 1 or choice > 5:
        print("Invalid choice! Try again.")
        continue

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result =", num1 / num2)

    elif choice == 4:
        print("Result =", num1 * num2)
