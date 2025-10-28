# Repeat the previous exercise, but use the Python's built-in sum function to compute the relevant sums without using loops. 

# For example, sum(range(2, 4)) evaluates to 5(=2+3). Do the same for all previous exercises. Make sure you get the same outputs.

n = int(input('enter an integer: '))

print(sum(range(3, n + 1)))
print(sum(range(3, n + 1, 2)))
print(sum(range(3, n + 1, 3)))