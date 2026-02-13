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

# first non repeating character in a string
'''
a = input()
res = {}
for i in a:
    res[i] = res.get(i,0) + 1
for i in a:
    if res[i] == 1:
        print(i)
        break
else:
    print("No non repeating character")
'''

# most frequent character in a string
'''
a = input()
res = {}
for i in a:
    res[i] = res.get(i,0) + 1
max_freq = max(res.values())
for i in res:
    if res[i] == max_freq:
        print(i)
        break
'''

# longest word in the string
'''
a = input().split()
l = ""
for i in a:
    if len(i) > len(l):
        l = i
print(l)
'''

# check if 2 strings anagrams
'''
a = input()
b = input()
print("Anagrams" if sorted(a) == sorted(b) else "Not an Anagram")
'''

# string compression 
'''
a = input()
res = {}
for i in a:
    res[i] = res.get(i,0) + 1
for key,value in res.items():
    print(f"{key}{value}",end="")
'''

# count words in a paragraph
'''
a = input().split()
c = 0
for i in a:
    c += 1
print(c)
'''