# Write a Python program to check whether two variables refer to the same memory location and
# print the result using appropriate operators.
'''
a = int(input())
b = float(input())
print(a == b) # checks whether the numbers are equal 
print(a is b) # check whether both a and b are in same memory object
'''

# Write a Python program to remove duplicate elements from a list and 
# display the result without changing the original order.
'''
inp = list(map(int,input().split()))
a = set(inp)
print(list(a))
'''

# Write a Python program to count the number of occurrences of each element in a list and 
# store the result in a dictionary.
'''
inp = list(map(int,input().split()))
a = {}

for i in inp:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1

print(a)
'''

# Write a Python program to find the intersection of two sets using set operators and display the output.
'''
inp1 = set(map(int,input().split()))
inp2 = set(map(int,input().split()))
a = inp1 & inp2
print(a)
'''

# Write a Python program to swap two numbers without using a third variable, using operators.
'''
a = 10
b = 20
a,b = b,a
print(a)
print(b)
'''

# Write a Python program to check whether a given number is even or odd using bitwise operators.
'''
a = int(input())
if a & 1 == 0:
    print("Even number")
else:
    print("Odd number")
'''

# Write a Python program to reverse a string using slicing and print the reversed string.
'''
inp = input()
print(inp[::-1])
'''

# Write a Python program to merge two dictionaries.
# If a key exists in both dictionaries, add their values.
'''
dict1 = eval(input())
dict2 = eval(input())
new_dict = dict1 | dict2
print(new_dict)
'''
# Write a Python program to evaluate the expression using arithmetic and logical operators and 
# print the final result:
# not 0 and 1 or 0
'''
print(not 0 and 1 or 0)
'''

# Write a Python program to find the maximum and minimum elements in a list without using built-in functions.
'''
inp = list(map(int,input().split()))
a = sorted(inp)
print("Minimum element is" , a[0] , "Maximum element is " , a[-1])
'''

# Write a Python program to demonstrate the difference between == and is using list datatypes.
'''
a = 10
b = 20
print(a == b) # returns false
print(a is b) # returns false
a = b
print(a is b)
'''

# merge 2 dictionaries
'''
d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}

res = {}
for key in d1:
    res[key] = d1[key]

for key in d2:
    res[key] = res.get(key,0) + d2[key]

print(res)
'''

# FREQUENCY COUNT in dictionaries
'''
inp = list(map(int,input().split()))
freq = {}

for i in inp:
    freq[i] = freq.get(i,0) + 1

print(freq)
'''

# COUNT CHARACTERS IN A STRING using dictionaries
'''
inp = input()

res = {}

for i in inp:
    res[i] = res.get(i,0) + 1

print(res)
'''

# Write a Python program to find and display the key having the maximum value and 
# the key having the minimum value in a dictionary. 
'''
d = {"pen": 15, "book": 40, "eraser": 5, "pencil": 25}

print("Key with maximum value:" , max(d,key=d.get))
print("Key with minimum value:",min(d,key=d.get))
'''

