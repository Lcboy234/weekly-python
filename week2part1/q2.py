# Write a program that asks the user to enter a string. 
# If the string contains at least one of every vowel (a, e, i, o, u), print 'All vowels are there!'. 
# Additionally, if the string starts with the letter a and ends with the letter z, print 'And it could be alphabetical!'.

# Hint: use in to determine if a given string is contained in another string. For example, 'a' in 'xyab' evaluates to True.

n = input('Enter a string: ')

if ('a' in n) and ('e' in n) and ('i' in n) and ('o' in n) and ('u' in n):
    print('All vowels are there!')

if n[0] == 'a' and n[-1] == 'z':
    print('And it could be alphabetical!')