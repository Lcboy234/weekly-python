import numpy as np
import math

def computeLength(v):
    return math.sqrt(np.dot(v, v))

a = np.array([1,-1])
b = np.array([1,1])
c = np.array([2,0])

print(computeLength(a), np.linalg.norm(a))
print(computeLength(b), np.linalg.norm(b))
print(computeLength(c), np.linalg.norm(c))