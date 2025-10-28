# Write a program that asks the user to enter a string, and using string slicing determines whether the string is a concatenation of three identical strings. 
# If so, print 'string is a triple concat of ' followed by the relevant substring; 
# otherwise, print 'string is not a triple concat'.

# For example, if the user enters 'hello,hello,hello,', 
# the output must be 'string is a triple concat of hello,'.

n = input('Enter a string: ')

if len(n) % 3 == 0:
    part_length = len(n) // 3
    first = n[0: part_length]
    second = n[part_length: 2*part_length]
    third = n[2*part_length: 3*part_length]

    if first == second == third:
        print(f'string is a triple concat of {first}')
    else:
        print('string is not a triple concat')
else:      
    print('string is not a triple concat')