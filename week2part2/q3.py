# Write a function min_max() that takes a string of digits as input and 
# returns a string consisting of the smallest and the largest integers in the input string.
 
# Do this by iterating over the elements of the string using the for...in loop. Do not use the built-in min() and max() functions.

# For example, min_max("31805") should return "08".

def min_max(digits):
    smallest = digits[0]
    largest = digits[0]

    for i in digits:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return(smallest + largest)

print(min_max("31805"))