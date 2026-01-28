# Q1. Chef is watching a movie that has a total duration of X minutes
# Chef watches the first Y minutes at normal speed
# The remaining part of the movie is watched at double speed 
# Calculate the total time in minutes chef spends watching the movie
'''
inp = list(map(int,input().split()))
a = inp[1]
b = int(a + (a/2))
print(b) 
'''

# Q2. Rahul appeared for N tests. The average score of these N tests is A.
# Rahul knows the score of N - 1 tests. The score of the remaining test is missing.
# Calculate the missing test score
'''
inp1 = int(input())
inp2 = list(map(int,input().split()))
inp3 = int(input())
a = inp1 * inp3
b = sum(inp2)
c = a - b
print(c)
'''

# A shopkeeper runs a store selling gadgets. Today, he is offering 2 successive discounts on an item.
    # The item is marked at M rupees
    # First, the shopkeeper gives a discount of A% on the marked price.
    # Then, he gives an additional discount of B% on the remaining amount.
# Additionally, the shopkeeper wants to calculate :
    # The total discount amount in rupees
    # The final priice after both discounts
    # Whether the final price is less than or equal to a customer's budget p
# Calculate all the above  
'''
inp = list(map(int,input().split()))
a = inp[1]
b = int((a/100) * inp[0])
c = inp[2]
d = int((c/100) * inp[0])
e = int(b+d)
print(e)  # total discount amount as integer
f = inp[0] 
g = int(f-e)
print(g) # Final price after both discounts as integer
# True if final price is less than or equal to the ciustomer's budget, Otherwise False
if g <= inp[-1]:
    print("True")
else:
    print("False")
'''

# A streaming platform is tracking movies watched by 3 users. Alice, Bob, and Carol
    # Each user has a watchlist of exactly 3 movies
    # You need to calculate
        # 1. Movies watched by all 3 users
        # 2. Movies watched by atleast 2 users
        # 3. Movies watched by exactly 1 user

# Input format : 
    # First line : 3 space separated strings - Alice's movies
    # Second line : 3 space separated strings - Bob's movies
    # Third line : 3 space separated strings - Carol's movies
# All movie names are single words(no spaces)

# Output format :
    # First line : Movies watched by all users (comma separated, alphabetical order)
    # Second line : Movies watched by at least 2 users (comma separated, alphabetical order)
    # Thirs line : Movies watched by exactly one user(comma separated, alphabetical order)
'''
alice = set(input().split())
bob = set(input().split())
carol = set(input().split())

all_three = alice & bob & carol # Union

at_least_two = (alice & bob) | (bob & carol) | (alice & carol) # Intersection

exactly_one = (alice | bob | carol) - at_least_two # subtraction

print(",".join(sorted(all_three)))
print(",".join(sorted(at_least_two)))
print(",".join(sorted(exactly_one)))
'''
