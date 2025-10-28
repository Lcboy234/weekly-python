# Repeat the previous exercise but sum only the odd numbers. 

# For example, if n=10, your program must print 24.

n = int(input('enter an integer: 10'))

odd_sum = 0

for i in range(3, n + 1, 2):
    odd_sum += i
print(odd_sum)