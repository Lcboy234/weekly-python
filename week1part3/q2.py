# Write a program that initialises a variable secret with a secret number between 0 and 10, 
# and then, proceeds to repeatedly ask the user to enter a number between 0 and 10 using a while loop until the secret number is correctly guessed.
# Once this happens, the program must print Well done! and terminate. 
# For example, if secret=4, then a possible interaction between your program and the user may look as follows:

# Enter a number between 0 and 10: 7
# Enter a number between 0 and 10: 8
# Enter a number between 0 and 10: 7
# Enter a number between 0 and 10: 2
# Enter a number between 0 and 10: 4
# Well done!
# Try the following two ways of implementing the above:

# Write a while loop that runs forever using True as the loop continuation condition, and use the break statement to exit the loop once the secret number is correctly guessed.
# Write a while loop having the comparison between the secret number and the user input as the loop continuation condition.

secret = 4

n = -4
while n != secret:
    n = int(input('Enter a number between 0 and 10: '))
    if n == secret:
        print('Well done!')