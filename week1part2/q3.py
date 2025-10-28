# Repeat the previous exercise but sum only the multiples of 3. 

# For example, if n=10, your program must print 18.

n = int(input('enter an integer: '))

sum = 0

for i in range(3, n + 1, 3):
    sum += i
print(sum)