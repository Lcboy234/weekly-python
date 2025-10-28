# In Python, it is possible to check if a string represents an integer by using the string object's method isdigit(). 

# For example:
# '123'.isdigit() returns True
# '1a3'.isdigit() returns False
# Write a program that asks the user to enter an integer n.

# Use isdigit to verify that the user’s input is indeed an integer. If it is, then proceed with the rest of the logic; 
# otherwise, print 'string is not a number' and exit. Try to use a single conditional statement with an extra elif.

# If the user's input is an integer, the program 
# prints n is greater than 10 if n > 10, 
# n is less than 10 if n < 10, and n is ten, in all other cases. 
# 
# Use an appropriate conditional statement (if-elif-else). You can assume that the inputs are valid integers.

n = input('please enter an integer: ')

if n.isdigit():
    new_n = int(n)
    if new_n > 10:
        print('n is greater than 10')
    elif new_n < 10:
        print('n is less than 10')
    else:
        print('n is 10')

print('string is not a number')