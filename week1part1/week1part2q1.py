# Write a program that asks the user to enter an integer n, and 
# prints n is positive if n > 0, 
# n is negative if n < 0, and n is zero, in all other cases. 
# 
# Use an appropriate conditional statement (if-elif-else). You can assume that the inputs are valid integers.

n = int(input("Please input an integer: "))

if n > 0:
    print('n is positive')

elif n < 0:
    print('n is negative')

else:
    print('n is zero')