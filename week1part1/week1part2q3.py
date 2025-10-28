# Write a program that asks the user to enter two integers a and b, 
# initialises an integer variable secret to store your "secret" number, and prints
# 'both numbers are positive', if a > 0 and b > 0,
# 'both numbers are negative', if a < 0 and b < 0,
# 'one number is 0', if either a = 0 or b = 0, and
# 'numbers have opposite signs', in all other cases.

# In addition, your program must also print
# 'you also guessed my secret number!' if either a or b is equal to your secret number, and
# 'no luck this time', otherwise.
# For example, if a = 5, b =  − 3, and the secret number is 5, your program must print

# numbers have opposite signs
# you also guessed my secret number!
# You can assume that the inputs are valid integers. There is no need to check the input validity.

a = int(input('input first integer: '))
b = int(input('input second integer: '))

secret = 8

if a > 0 and b > 0:
    print('both numbers are positive')
elif a < 0 and b < 0:
    print('both numbers are negative')
elif a == 0 or b == 0:
    print('one number is 0')
else:
    print('numbers have opposite signs')

if a or b == secret:
    print('you also guessed my secret number!')
else:
    print('no luck this time')