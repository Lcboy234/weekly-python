# def is_leading_string_repeated(s):

#     n = len(s)

#     for i in range(1, n // 3 + 1):

#         part = s[-i:]

#         if s[-i * 3:] == part * 3:

#             return part
        
#     return None

# print(is_leading_string_repeated('abcabcabcabc'))




# Write a program that asks the user to enter a string s, 
# and outputs the number of times the string 'tart' appears in s.

# For example, if the input is iliketartartandmoretart, the output must be 3.

# Note that simply calling s.count('tart') may not produce a correct answer 
# as it only counts the number of non-overlapping substrings.

# That is, in the above example, 'iliketartartandmoretart'.count('tart') 
# evaluates to 2 since the second occurrence of tart overlaps the first one.

n = input('Enter a string: ')

word = 'tart'

count = 0
for i in range(len(n) - len(word) + 1):
    if n[i: i + len(word)] == word:
        count += 1
print(count)