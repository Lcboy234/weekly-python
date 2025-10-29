# Write a function sort3() that takes three integers as input arguments and 
# returns a tuple consisting of the input numbers sorted in the increasing order of their values.

# For example, sort3(120, 3, 23) should return (3, 23, 120).

def sort3(a, b, c):
    if a <= b and a <= c:
        smallest = a
        if b <= c:
            middle = b
            largest = c
        else:
            middle = c
            largest = b
    elif b <= a and b <= c:
        smallest = b
        if a <= c:
            middle = a
            largest = c
        else:
            middle = c
            largest = a
    else:
        smallest = c
        if a <= b:
            middle = a
            largest = b
        else:
            middle = b
            largest = a
    
    return(smallest, middle, largest)

print(sort3(120, 3, 23))