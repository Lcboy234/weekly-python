# Write a function extract_strings that takes three arguments with arbitrary types, 
# and returns a string with all the arguments that are strings concatenated together.

# For example, extract_strings(('foo' , 5, 'aaa')) should return ('fooaaa').

# Hints:

# Use type(x) to determine the type of variable x.

# The keyword to denote the string type in Python is str.

def extract_strings(a, b, c):
    final_string = ""
    if type(a) == str:
        final_string += a
    if type(b) == str:
        final_string += b
    if type(c) == str:
        final_string += c

    return final_string

print(extract_strings('foo' , 5, 'aaa'))