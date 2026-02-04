'''
# WAP to count how many factors of 5bare present in the given list 

a = list(map(int,input().split(",")))
l = []
for i in a:
    if i % 5 == 0:
        l.append(i)
print(len(l))
'''
'''
a = tuple(map(int,input().split()))
c = 0
for i in a:
    if i > c:
        c = i
print(c)
'''
'''
# WAP to calculate the average of all elements in the tuple using a for loop,
# without using the built-in functions, such as sum() and len()

a = tuple(map(int,input().split(",")))
s = 0
n = 0
for i in a:
    s += i
    n += 1
avg = s/n
print(avg)
'''
'''
# WAP to check whetehr the given number is a prime number using a for loop

a = int(input())
isprime = True
if a == 1:
    isprime = True
else:
    for i in range(2,a):
        if a % i == 0:
            isprime = False
            break
if isprime == True:
    print("Prime")
else:
    print("Not Prime")
'''
'''
# WAP to count the number of digits and the number of alphabetic characters separately using a for loop.

a = input()
l = list(a)
d = 0
n = 0
for i in l:
    if i.isalpha():
        d += 1
    else:
        n += 1
print("Digits : ", n)
print("Characters : ", d)
'''