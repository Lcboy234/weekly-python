# Write a program that asks the user to enter an integer n, and prints n!. 
# Recall that n! stands for the factorial of n, which is 1 if n = 0, and 1 × 2 × … × n if n > 0. 
# For example, if n = 10, your program must print

# 3628800
# Modify the program you wrote earlier to handle the case of n = 0 using an appropriate conditional statement. 
# Test your solution on a few sample inputs to 
# verify that it both continues to work correctly for n > 0, and outputs 1 for n = 0.

n = int(input('input an integer: '))

if n == 0:
    print(1)

elif n > 0:

    result = 1
    for i in range(1, n + 1):
        result = result * i
    print(result)