def area(shape, n):
    #    replace pass with a line to return the area
    #    of a generic shape with a parameter of n
    return shape(n)

def circle(radius):
    """
    Input: radius, a positive float
    Returns the area of a circle with the given radius
    """
    return 3.14*radius**2

def square(length):
    """
    Input: length, a positive float
    Returns the area of a square with sides of the given length
    """
    return length*length

print(area(circle,5))  # example function call
print(area(circle,10))
print(area(square,5))
print(area(circle,2))