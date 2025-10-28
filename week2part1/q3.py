# Write a program that asks the user to enter a string, 
# and returns the number of vowels (a, e, i, o, u) appearing at all odd indices. 

# For example, if the user enters 'eggs over aesy', then your program must output 3.

n = input('Enter a string: ')

vowels = 'aeiou'

count = 0

for i in range(len(n)):
    if i % 2 == 1 and n[i] in vowels:
        count += 1

print(count)