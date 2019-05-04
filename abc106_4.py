import numpy as np
import math

def main():
    N, M, Q = map(int, input().split())
    matrix = np.zeros((N + 1, N + 1))
    cmatrix = np.zeros((N + 1, N + 1))
    for i in range(M):
        left, right = map(int, input().split())
        matrix[left][right] += 1
    # print(matrix)

    for i in range(1, N+1):
        for j in range(1, N+1):
            cmatrix[i][j] = cmatrix[i][j - 1] + matrix[i][j]
    
    for i in range(Q):
        left, right = map(int, input().split())
        num = 0
        for j in range(left, right + 1):
            num += cmatrix[j][right] - cmatrix[j][left - 1]
        print(int(num))

if __name__ == '__main__':
    main()