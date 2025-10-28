# Write a program that asks the user for a string and prints its first and last character. 
# If the string has length one, it should just print one character. 
# If the string is empty, is should just print a new line.

# Hints:

# Use the built-in function len to determine the length of a string. For example, len('abc') evaluates to 3.

# To determine whether a string is empty, you can either compare its length with 0, or compare it directly against '', which represents the empty string.

n = input('Enter a string: ')

if len(n) == 1:
    print(n)
elif len(n) == 0:
    n = input('Enter a string: ')
else:
    print(n[0])
    print(n[-1])