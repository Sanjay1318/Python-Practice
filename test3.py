# Divisible Sum Pairs Count
# Given an integer array arr of size N and an integer K, count the number of pairs (i, j) such that:
#    i < j
#    (arr[i] + arr[j]) % K == 0
# input : 
#       N = 6  
#       arr = [1, 3, 2, 6, 1, 2]  
#       K = 3
# output :
#       5
'''
N = int(input())
arr = list(map(int,input().split(",")))
K = int(input())

count = 0

for i in range(N):
    for j in range(i + 1, N):
        if (arr[i] + arr[j]) % K == 0:
            count += 1

print(count)
'''

#Reverse a Given Number
# Write a program to reverse a given positive integer.
'''
N = int(input())
reverse = 0

while N > 0:
    digit = N % 10
    reverse = reverse * 10 + digit
    N = N // 10

print(reverse)
'''

# Reverse Only Letters
# Reverse only alphabet characters in a string. Do not change the position of digits.
# input : a1b2c3
# output : c1b2a3
'''
s = input()
letters = []

for ch in s:
    if ch.isalpha():
        letters.append(ch)

letters.reverse()

result = ""
letter_index = 0

for ch in s:
    if ch.isalpha():
        result += letters[letter_index]
        letter_index += 1
    else:
        result += ch

print(result)
'''

# Arrow Pattern Printing
# Print an upward arrow properly centered.
'''
N = int(input())
# Upper triangle
for i in range(1, N + 1):
    spaces = N - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
# Arrow tail
for i in range(N):
    print(" " * (N - 1) + "|")
'''

# Butterfly Pattern Printing
# Print a butterfly pattern that is symmetric horizontally and vertically.
'''
N = int(input())
# Upper part
for i in range(1, N + 1):
    stars = "*" * i
    spaces = " " * (2 * (N - i))
    print(stars + spaces + stars)
# Lower part
for i in range(N - 1, 0, -1):
    stars = "*" * i
    spaces = " " * (2 * (N - i))
    print(stars + spaces + stars)
'''
    