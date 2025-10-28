# Write a program squareSum.py that asks the user to 
# enter a positive integer n and, using a while loop, 

# computes the sum 1**2 + 2**2 + … + n**2. If you try the program with input 6 you should get 91.

n = int(input('enter an integer: '))

sum = 0
i = 0

while i <= n:
    sum += i ** 2
    i += 1

print(sum)