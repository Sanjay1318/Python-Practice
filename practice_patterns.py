'''# square
n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end = " ")
    print()

# right angle triangle
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end = " ")
    print()

# inverted right angle triangle
n = int(input())
for i in range(0,n):
    for j in range(n-i+1):
        print("*",end = " ")
    print()

# right sided triangle
n = int(input())
for i in range(n):
        for j in range(i,n):
            print(" ",end = " ")
        for j in range(i+1):
            print("*",end = " ")
        print()

# inverted right sided triangle
n = int(input())
for i in range(n):
        for j in range(i+1):
            print(" ",end = " ")
        for j in range(i,n):
            print("*",end = " ")
        print()

# Hill pattern
n = int(input())
for i in range(n):
        for j in range(i,n):
            print(" ",end = " ")
        for j in range(i+1):
            print("*",end = " ")
        for j in range(i):
            print("*",end = " ")
        print()

# Inverted Hill pattern
n = int(input())
for i in range(n):
        for j in range(i+1):
            print(" ",end = " ")
        for j in range(i,n):
            print("*",end = " ")
        for j in range(i+1,n):
            print("*",end = " ")
        print()

# Diamond pattern
n = int(input())
for i in range(n):
        for j in range(i,n):
            print(" ",end = " ")
        for j in range(i+1):
            print("*",end = " ")
        for j in range(i):
            print("*",end = " ")
        print()
for i in range(n):
        for j in range(i+1):
            print(" ",end = " ")
        for j in range(i,n):
            print("*",end = " ")
        for j in range(i+1,n):
            print("*",end = " ")
        print()

# Double Hill pattern
n = int(input())
for i in range(n):
    # Left spaces
    print("  " * (n - i), end="")

    # Left hill
    print("* " * (2 * i + 1), end="")

    # Middle spaces
    print("  " * (n - i), end="")

    # Right hill
    print("* " * (2 * i + 1))

# Pyramid pattern
n = int(input())
for i in range(n):
    # Print leading spaces
    print(" " * (n - i - 1), end="")
    
    # Print stars
    print("* " * (i + 1))

# Inverted Pyramid pattern
n = int(input())
for i in range(n):
    # Print leading spaces
    print(" " * i, end="")
    
    # Print stars
    print("* " * (n - i))

# Butterfly pattern
n = int(input())
for i in range(n):
    # Left wing
    print("* " * (i + 1), end="")
    
    # Spaces between wings
    print("  " * (n - i - 1), end="")
    
    # Right wing
    print("* " * (i + 1))
for i in range(n):
    # Left wing
    print("* " * (n - i), end="")
    
    # Spaces between wings
    print("  " * i, end="")
    
    # Right wing
    print("* " * (n - i))

# Sandglass pattern
n = int(input())
for i in range(n): 
    # Print leading spaces
    print(" " * i, end="")
    
    # Print stars
    print("* " * (n - i))
for i in range(n):
    # Print leading spaces
    print(" " * (n - i - 1), end="")
    
    # Print stars
    print("* " * (i + 1))

# Left Pascal's Triangle
n = int(input())
for i in range(n):
    # Print stars
    print("* " * (i + 1))
for i in range(n):
    # Print stars
    print("* " * (n - i - 1))
'''

# Right Pascal's Triangle
n = int(input())
for i in range(n):
    # Print spaces
    print(" " * (n - i - 1), end="")
    
    # Print stars
    print("* " * (i + 1))
for i in range(n):
    # Print spaces
    print(" " * i, end="")
    
    # Print stars
    print("* " * (n - i - 1))