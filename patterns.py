# Factorial of a Number

num = int(input("Enter number: "))
fact = 1

for i in range(1, num+1):
    fact *= i

print("Factorial =", fact)


# Fibonacci Series

n = int(input("Enter how many terms: "))
a, b = 0, 1
print(a, b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c


# Palindrome(Number)

num = int(input("Enter number: "))
rev = 0
temp = num

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if rev == num:
    print("Palindrome")
else:
    print("Not Palindrome")


# Palindrome(String)

s = input("Enter string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Prime Number Check

num = int(input("Enter number: "))

if num < 2:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")


# Armstrong Number  Example: 153 → 1³ + 5³ + 3³ = 153

num = int(input("Enter number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")


# Right Angle Triangle
"""
    *
    **
    ***
    ****
"""

n = int(input("Enter rows: "))

for i in range(1, n+1):
    print("*" * i)


# Inverted Right Angle Triangle
"""
****
***
**
*
"""

n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    print("*" * i)


# Pyramid Pattern
"""
   *
  ***
 *****
*******
"""

n = int(input("Enter rows: "))

for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))


# Number Triangle
"""
1
12
123
1234
"""

n = int(input("Enter rows: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()


# Reversed Number Triangle
"""
1234
123
12
1
"""

n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()


# Sum of digits

num = int(input("Enter number: "))
s = 0

while num > 0:
    s += num % 10
    num //= 10

print("Sum =", s)


# Reverse a number

num = int(input("Enter number: "))
rev = 0

while num > 0:
    rev = rev*10 + num%10
    num//=10

print("Reverse =", rev)
