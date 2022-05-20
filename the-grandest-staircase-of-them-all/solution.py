import numpy as np
def solution(n):
    size = n + 1
    mat = [[0]*size for _ in range(size)]
    mat[0][0] = 1
    for prev in range(1, size):
        for left in range(0, size):
            mat[prev][left] = mat[prev - 1][left]
            if left >= prev:
                mat[prev][left] += mat[prev - 1][left - prev]
        print(np.matrix(mat))
    return mat[n][n] - 1


print(solution(6))
