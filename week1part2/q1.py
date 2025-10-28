# Write a program that asks the user to enter an integer n, 
# and, using a for loop along with an appropriately selected range(), 
# computes and prints out the sum of all integers from 3 to n. 

# For example, if n=10, your program must print 52. 
# You can assume that users will enter valid inputs. 
# There is no need to check for the input validity.

n = int(input('enter an integer: '))

sum = 0
for i in range(3, n + 1):
    sum += i
print(sum)