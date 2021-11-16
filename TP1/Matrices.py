import numpy as np

B = [[1,2,3],[1,2,3],[1,2,3]]
C = [[4,5,6],[4,5,6],[4,5,6]]


def multiplication(B,C):
    A = np.zeros(shape=(len(B),len(C[0])))
    print(A)
    for i in range(0,len(B)):
        for j in range(0,len(C[0])):
            for k in range(0,len(C)):
                A[i][j] += B[i][k] * C[k][j]
    return A

print(multiplication(B,C))

