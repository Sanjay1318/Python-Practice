# Create an integer and a float, add them, and print the data type of the result.
'''
a = int(input())
b = float(input())
c = a + b
print(c , type(c))
'''

# Store a string and print the number of characters in it.
'''
inp = input()
print(len(inp))
'''

# Add an integer and a boolean value and print the result.
'''
a = 2
b = True
print(a+b)
'''

# Perform floor division between a float and an integer and print the data type of the result.
'''
a = 20
b = 12.4
c = a//b
print(c , type(c))
'''

# Store a string and print its third character.
'''
inp = input()
print(inp[2])
'''

# Create a list of numbers and print its data type.
'''
lst = [1,2,3,4,5]
print(type(lst))
'''

# Convert zero into a boolean and print the result.
'''
a = 0
b = bool(a)
print(b)
'''

# Divide two integers and print the output.
'''
num1 = int(input())
num2 = int(input())
print(num1 / num2)
'''

# Store a number as a string and print its data type.
'''
a = "23"
print(type(a))
'''

# Add True and False and print the data type of the result.
'''
print(type(True + False))
'''

# Store a string and print a substring using slicing (not the first or last character).
'''
inp = input()
print(inp[1:-1])
'''

# Create a list, assign it to another variable, modify one element using the second variable, and print the first list.
'''
lst = list(map(int,input().split(",")))
a = lst
a[4] = lst[4]
print(lst)
'''

# Create a tuple and repeat it twice, then print the result.
'''
tup = tuple(map(int,input().split(",")))
print(tup * 2)
'''

# Perform exponentiation on two integers and print the data type of the result.
'''
a = int(input())
b = int(input())
c = a ** b
print(c , type(c))
'''

# Repeat a string multiple times and print the length of the final string.
'''
a = input()
b = a * 2
print(b , len(b))
'''

# Create a list and print every alternate element using slicing.
'''
lst = list(map(int,input().split(",")))
print(lst[::2])
'''

# Convert a non-zero float into a boolean and print the result.
'''
a = float(input("Enter a non - zero float value : "))
print(bool(a))
'''

# Multiply a boolean value with an integer and print the data type of the result.
'''
a = int(input("Enter a integer value : "))
b = True
c = a * b
print(c, type(c))
'''

# Reverse a string using slicing and print it.
'''
a = input()
print(a[::-1])
'''

# Create a variable with a single value inside parentheses and print its data type.
'''
a = ("2")
print(type(a))
b = (2)
print(type(b))
'''

# Create a tuple with a single element and print its data type.
'''
tup = (1,)
print(type(tup)) 
'''

# Create a list, duplicate it using multiplication, modify one element in the duplicated list, and print the original list.
'''
lst = list(map(int,input().split(",")))
a = lst * 2
a[1] = lst[2]
print(lst)
'''

# Multiply a numeric string with an integer and print the result.
'''
a = "1234"
print(a * 2)
'''

# Add boolean values multiple times and print the result.
'''
a = True
b = False
c = a + b + b + a
print(c)
'''

# Add two decimal values that look equal mathematically and print the data type of the result.
'''
print(type(1.23 + 1.23))
'''

# Convert an empty list into a boolean and print the result.
'''
lst = list(map(int,input().split(",")))
a = lst.clear()
print(bool(a))
'''

# Try slicing a string beyond its length and print the result.
'''
a = "Python"
print(a[0:len(a)+3])
'''

# Slice a list in such a way that the result is still a list and print its data type.
'''
lst = list(map(int,input().split(",")))
a = lst[1:4]
print(a, type(a))
'''

# Store None in a variable and print its data type.
'''
a = None
print(type(a))
'''

# Concatenate two strings and print the length of the final string.
'''
a = input()
b = input()
c = a + b
print(c , len(c))
'''

# Given a string containing characters and numbers, find and print the sum of the numbers present in the string.
'''
a = "aaa123bb45cc6"
b = set(a)
s = sorted(b)
c = s[:6]
d = list(map(int,c))
e = sum(d)
print(e)
'''
