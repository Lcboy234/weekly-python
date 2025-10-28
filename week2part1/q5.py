# Write a program that asks the user to enter a string s, 
# and outputs the number of times the string 'tart' appears in s.

# For example, if the input is iliketartartandmoretart, the output must be 3.

# Note that simply calling s.count('tart') may not produce a correct answer 
# as it only counts the number of non-overlapping substrings.

# That is, in the above example, 'iliketartartandmoretart'.count('tart') 
# evaluates to 2 since the second occurrence of tart overlaps the first one.
# 23 - 4 = 19 + 1 = 20
s = input('Enter a string: ')

target = 'tart'

count = 0

# use range to lock it in bound (loop until last 4 digit)
for i in range(len(s) - len(target) + 1):
    # if s[0:4]
    if s[i: i + len(target)] == target:
        count += 1

print(count)