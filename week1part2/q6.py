# Write a program that asks the user to enter an integer n, and prints n!. 
# Recall that n! stands for the factorial of n, which is 1 if n=0, and 1 × 2 × … × n if n > 0. 
# For example, if n=10, your program must print

# 3628800
# You can assume that the input is a valid positive integer, that is, n > 0.

n = int(input('enter an integer: '))

if n == 0:
    print(1)
elif n > 0:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)