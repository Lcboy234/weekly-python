import numpy as np

A = np.array([[1,2,3],[4,5,6]])

def selectMatrixEntry(M, i, j):
    return M[i][j]

print(selectMatrixEntry(A, 1, 0))