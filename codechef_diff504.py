# Codechef difficulty : 504 program (Subscription)
inp1 = int(input("price per each subscription:"))
inp2 = int(input("Enter number of users:"))
a = inp2 / 6
if a.is_integer():
    print(int(a)*inp1)
else:
    print((int(a)+1) * inp1)

