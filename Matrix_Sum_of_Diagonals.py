# Function to calculate the absolute difference
# between the sums of the primary and secondary diagonals
def sum_of_Diagonals(arr):
    n = len(arr)                         # n = number of rows (and also columns since it's a square matrix)
   
    left_sum = 0         # Variables to store diagonal sums     # Primary Diagonal Sum
    right_sum = 0                                               # Secondary Diagonal Sum

    for i in range(n):                      # Loop through each row index
        left_sum += arr[i][i]               # Primary Diagonal  elements like arr[0][0], arr[1][1], arr[2][2] ...
        right_sum += arr[i][n-1-i]          # Secondary Diagonal        arr[0][n-1], arr[1][n-2], arr[2][n-3] ...

    return abs(left_sum - right_sum)        # Return absolute difference between the two diagonal sums

n = int(input("Enter a Number : "))         # Take matrix size input
arr = []                                    # Create an empty matrix (list of lists)

for i in range(n):                          # Take matrix input row by row
    arr.append(list(map(int,input().split())))           # Convert space-separated input into list of integers

print(sum_of_Diagonals(arr))                    # Call function and print result