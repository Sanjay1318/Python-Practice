# missing number in a number sequence
'''
a = list(map(int,input().split()))
c = 0
for i in range(len(a)):
    if a[i] != i+1:
        print(i+1) 
        break
'''
# character occurence count using only dictionary
'''
a = input()
res = {}
for i in a:
    res[i] = res.get(i,0) + 1
print(res)
'''

# reverse each word in a string
'''
a = input().split()
c = []
for i in a:
    c.append(i[::-1])
print(c)
'''

# find even and odd from list using for loop
'''
a = list(map(int,input().split()))
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even:",*even)
print("Odd:",*odd)
'''

# sum of digits in a number
'''
a = int(input())
s = str(a)
lst = []
for i in s:
    lst.append(int(i))
print(sum(lst))
'''

# find even and odd index elements from the list
'''
a = input().split()
even = []
odd = []
for i in range(len(a)):
    if i % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
print("Even ", *even)
print("Odd ",*odd)
'''

# find vowels and consonants in a string
'''
a = input().lower()
v = []
c = []
vowels = "aeiou"
for i in a:
    if i in vowels:
        v.append(i)
    else:
        c.append(i)
print(f"Number of vowels in the given string are {len(v)}")
print("They are", *v)
print(f"Number of consonants in the given string are {len(c)}")
print("They are", *c)
'''