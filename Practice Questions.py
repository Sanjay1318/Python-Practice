# Practice Questions
# Q1. Write a program to input 2 numbers and print there sum
"""
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
sum = a + b
print(sum)
"""

# Q2. Write a program to input side of a square and print its area
"""
side = int(input("Enter the length of side of a square: "))
area = side * side
print("The area of the Square is: " + str(area))
"""

# Q3. Write a program to input 2 float point numbers and print there average
"""
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
average = (num1 + num2) / 2
print(average)
"""

# Q4. WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False.
"""
a = int(input("Enter Number A: "))
b = int(input("Enter Number B: "))
if a >= b:
    print("True")
else:
    print("False")
"""

# Q 5. WAP to input user’s first name & print its length.
"""
first_name = str(input("Enter Your First Nmae: "))
length = len(first_name)
print("The Lenght of the First Name is: " + str(length))
"""

# Q 6. WAP to find the occurrence of ‘$’ in a String.
"""
String = input("Enter a String: ")
count_value = String.count("$")
print(count_value)
"""

# Q 7. Write a Python program to input the marks of a student and print the grade according to the following criteria:
#   If marks are greater than or equal to 90, print “A”
#   If marks are less than 90 but greater than or equal to 80, print “B”
#   If marks are less than 80 but greater than or equal to 70, print “C”
#   If marks are less than 70, print “D”
"""
marks = float(input("Enter Marks: "))
if marks >= 90:
    print("A")
elif marks < 90 and marks >= 80:
    print("B")
elif marks < 80 and marks >= 70:
    print("C")
else:
    print("D")
"""

# WAP to check if a number entered by the user is odd or even.
"""
num = int(input("Enter a Number: "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")
"""

# WAP to find the greatest of 3 numbers entered by the user.
"""
num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
num3 = int(input("Enter Number3: "))

if num1 > num2 and num1 > num3:
    print("Greatest Number is: " + str(num1))
elif num2 > num1 and num2 > num3:
    print("Greatest Number is: " + str(num2))
else:
    print("Greatest Number is: " + str(num3))
"""

# WAP to check if a number is a multiple of 7 or not.
"""
num = int(input("Enter a Number: "))
if num % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a Multiple of 7")
"""

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
"""
movie = []
for i in range(3):
    movie_name = str(input("Enter Movie Names : "))
    movie.append(movie_name)

print(movie)
"""

# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
"""
number = []
for i in range(5):
    num = str(input("Enter Element : "))
    number.append(num)

temp = number.copy()
temp.reverse()

if number == temp:
    print("Palindrome")
else:
    print("Not A Palindrome")
"""

# WAP to count the number of students with the “A” grade in the following tuple.
#                [”C”,“D”,“A”,“A”,“B”,“B”,“A”]
"""
grades = ("C","D","A","A","B","B","A")
num = grades.count("A")
print("Number of times A Grade appeares is : " + str(num))
"""

# Store the above values in a list & sort them from “A” to “D”.
"""
grades = ("C","D","A","A","B","B","A")
grade_list = list(grades)
grade_list.sort()
print("The Grades In Ascending Order are : " , grade_list)
"""

# Dictionary Syntax with Example
"""
student = {"name": "Sanjay", "age": 21, "branch": "CSE"}

for key in student:
    print(key, "=", student[key])
"""

# Store following word meanings in a python dictionary :
#       table : “a piece of furniture”,“list of facts & figures”
#       cat : “a small animal”
"""
words = {"table" : ["a piece of furniture","list of facts & figures"],"cat" : ["a small animal"]}
for word in words:
    print(word, ":", words[word])
"""

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”
"""
subjects = ["python","java","C++","python","javascript","java","python","C++","C"]
unique_subjects = set(subjects)
print("The total number of classrooms required are : ", len(unique_subjects))
"""

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
"""
marks = {}

sub1_name = str(input("Enter First Subject : "))
sub1_marks = float(input("Enter First Subject Marks : "))
marks[sub1_name] = sub1_marks

sub2_name = str(input("Enter Second Subject : "))
sub2_marks = float(input("Enter Second Subject Marks : "))
marks[sub2_name] = sub2_marks

sub3_name = str(input("Enter Third Subject : "))
sub3_marks = float(input("Enter Third Subject Marks : "))
marks[sub3_name] = sub3_marks

print("\nMarks Detalis")

for subject,mark in marks.items():
    print(f"{subject}: {mark}")
"""

# Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
"""
set1 = (9,"9.0")
print(set1)
"""

# Print numbers from 1 to 100.
"""
for i in range(1,101):
    print(i)
"""

# Print numbers from 100 to 1.
"""
for i in range(100,0,-1):       # range(start, stop, step)
    print(i)
"""

# Print the multiplication table of a number n.
"""
num = int(input("Enter a number : "))

for i in range(1,11):
    table = num * i
    print(table)
    table += 1
"""

# Print the elements of the following list using a loop:
#       [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
"""
for i in range(1,11):
    temp = i * i
    print(temp)
    temp += 1
"""

# Search for a number x in this tuple using loop:
#       [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
"""
num_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

search_num = int(input("Enter a Number to Search: "))

if search_num in num_tuple:
    print("Present in the Tuple")
else:
    print("Not Present in the Tuple")
"""

# WAP to find the sum of first n numbers. (using while)
"""
num = int(input("Enter a number: "))
i = 1
total = 0

while i <= num:
    total += i
    i += 1

print("sum of first ", num , "numbers is", total)
"""

# WAP to find the factorial of first n numbers. (using for)
"""
n_number = int(input("Enter a Number : "))
fact = 1

for i in range(1,n_number + 1):
    fact = fact * i
    print("Factorial of " , i , "is" , fact)
"""

# WAF(function) to print the length of a list. ( list is the parameter)
"""
def print_length(lst):
    print("Length of the List is : " , len(lst))

nums = [1,2,3,4,"a","2"]
print_length(nums)
"""

# WAF to print the elements of a list in a single line. ( list is the parameter)
"""
def print_list(lst):
    for item in lst:
        print(item, end = " ")      #  end = " " keeps printing on the same line instead of new line.

nums = [1,2,3,4,"a","2"]
print_list(nums)
"""

# WAF to find the factorial of n. (n is the parameter)
"""
def factorial(n):
    fact = 1
    for i in range(1 , n + 1):
        fact *= i
    print("Factorial of " , n , "is" , fact)

factorial(5)
"""

# WAF to convert USD to INR.
"""
def currency_conversion(usd):
    inr = usd * 83
    print(usd , "USD is" , inr , "INR")

currency_conversion(10)
"""

# Write a recursive function to calculate the sum of first n natural numbers.
"""
def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n - 1)
    
print(sum(5))
"""

# Write a recursive function to print all elements in a list.
#       Hint : use list & index as parameters.
"""
def lst(n , index = 0):
    if index == len(n):
        return
    print(n[index])
    lst(n , index + 1)      # recursive call

nums = [1,2,3,4,5,6]
lst(nums , 0)
"""

# Fibonacci Series.  Start with 0,1 → next number = sum of previous two
"""
n = int(input("Enter a Number : "))
a = 0
b = 1
for i in range(n):
    print(a , end = " ")
    a = b
    b = a + b
"""

# Palindrome (Number / String).  Same forward and backward (121, madam)
"""
n = input("Enter a Number / String : ")
rev = n[::-1]       # reverse a string

if rev == n:
    print("Palindrome")
else:
    print("Not a Palindrome")
"""

# Armstrong Number.  Sum of digits³ = number.  Example → 153 = 1³ + 5³ + 3³
"""
n = int(input("Enter a Number : "))
temp = n
s = 0

while temp > 0:
    d = temp % 10
    s += d ** 3
    temp = temp // 10

if s == n:
    print("Arm Strong Number")
else:
    print("Not an Arm Strong Number")
"""

# Prime Number. Prime → divisible only by 1 & itself
"""
n = int(input("Enter a Number to check whether it's a prime number or not : "))
flag = True

if n < 2:
    flag = False

for i in range(2 , n):
    if n % i == 0:
        flag = False
        break

if flag == True:
    print("Prime Number")
else:
    print("Not A Prime Number")
"""

# Sum of Digits. Logic: extract last digit repeatedly
"""
n = int(input("Enter a Number : "))
s = 0
while n > 0:
    s += n % 10
    n = n // 10

print(s)
"""

# Factorial
"""
n = int(input("Enter a Number : "))
fact = 1

for i in range(1 , n + 1):
    fact *= i
    
print(fact)
"""

# Right Angled Triangle -- Pattern
"""
n = int(input("Enter a Number : "))
for i in range(1 , n + 1):
    print("*" * i)
"""

# Numbered Right Angled Triangle -- Pattern
"""
n = int(input("Enter a Number : "))

for i in range(1 , n + 1):
    for j in range(1, i + 1):
        print(j , end="")
    print()
"""

# Pyramid Pattern
"""
n = int(input("Enter a Number : "))

for i in range(1 , n + 1):
    print(" "*(n-i), "*"*(2*i-1))

"""

# Create a new file “practice.txt” using python. Add the following data in it:
"""
file = open("practice.txt","w")

file.write("Hi everyone\nwe are learning file I/0\nusing Java.\nI like programming in Java")

file.close()
"""

# WAF that replace all occurrences of “java” with “python” in above file.
"""
def replace_java_with_python():
    file = open("practice.txt","r")
    data = file.read()
    file.close()

    data = data.replace("Java","Python").replace("java","python")

    file = open("practice.txt","w")
    file.write(data)
    file.close()

replace_java_with_python()      # calling the function
"""

# Search if the word “learning” exists in the file or not.
"""
file = open("practice.txt","r")
data = file.read()
file.close()

if "learning" in data:
    print("The word 'learning' exists in the file.")
else:
    print("The word 'learning' does not exists in the file.")
"""

# WAF to find in which line of the file does the word “learning” occur first.Print -1 if word not found.
"""
def find_word_learning():
    file = open("practice.txt","r")
    lines = file.readlines()
    file.close()

    for i , line in enumerate(lines,start=1):
        if "learning" in line:
            print("Present")
            return
        
    print("-1")

find_word_learning()
"""

# From a file containing numbers separated by comma, print the count of even numbers.
        # read numbers from file → split by comma → convert to int → count evens.
"""
file = open("numbers.txt","r")      # Assume the file name is numbers.txt
data = file.read()
file.close()

numbers = data.split(",")       # split using a comma(,)
count = 0

for n in numbers():
    if int(n.strip()) % 2 == 0:
        count += 1

print("Even numbers counnt is : " , count)
"""

# Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
"""
class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = int(m1)
        self.m2 = int(m2)
        self.m3 = int(m3)

    def print_average(self):
        average = (self.m1 + self.m2 + self.m3)/3
        print("Average of marks", self.name, "=", average)

name = input("Enter name: ")
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

s1 = Student(name,m1,m2,m3)
s1.print_average()
"""

# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.
"""
class Account:
    def __init__(self, balance, account_number):
        self.balance = int(balance)
        self.account_number = int(account_number)

    def credit(self, amount):
        self.balance += amount
        print("Amount Credited : " , amount)

    def debit(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Debited : " , amount)
        else:
            print("Insufficient Balance")

    def print_balance(self):
        print("Account Number : ", self.account_number)
        print("Current Balance : ", self.balance)


acc1 = Account(2000,12345)

acc1.print_balance()
acc1.credit(2000)
acc1.debit(1000)
acc1.print_balance()
"""