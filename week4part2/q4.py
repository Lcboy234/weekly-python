import numpy as np
import math

def unit(v):
    bottom = math.sqrt(np.dot(v, v))
    if bottom == 0:
        raise ValueError("Cannot compute unit vector of zero length vector.")
    return v / bottom

a = np.array([1,-1])
b = np.array([1, 1])
c = np.array([2, 0])

print(unit(a))
print(unit(b))
print(unit(c))