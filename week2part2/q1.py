# Write a function max3() that takes three integers as input arguments and returns the largest of them. 
# Include a docstring describing the inputs, outputs, and what is being computed

def max3(a, b, c):
    """
    Returns the largest of three integers.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        int: The largest of the three input integers.
    """
    # Compare the three numbers
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max3(3, 7, 5))