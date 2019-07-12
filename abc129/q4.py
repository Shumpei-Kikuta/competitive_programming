import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)
from collections import deque


def search_y(i, j, matrix):
    """i, j について，y方向を埋める
    """
    to_plus = 0
    to_minus = 0
    while(True):
        to_plus += 1
        if (matrix[i + to_plus][j][0] == 0):
            continue
        else:
            to_plus -= 1
            break
    while(True):
        to_minus += 1
        if (matrix[i - to_minus][j][0] == 0):
            continue
        else:
            to_minus -= 1
            break
    sum_ = to_plus + to_minus + 1
    for i2 in range(0, to_plus + 1):
        matrix[i + i2][j][0] = sum_
    for i2 in range(0, to_minus + 1):
        matrix[i - i2][j][0] = sum_
    return matrix

def search_x(i, j, matrix):
    """i, j について，y方向を埋める
    """
    to_plus = 0
    to_minus = 0
    while(True):
        to_plus += 1
        if (matrix[i][j + to_plus][1] == 0):
            continue
        else:
            to_plus -= 1
            break
    while(True):
        to_minus += 1
        if (matrix[i][j - to_minus][1] == 0):
            continue
        else:
            to_minus -= 1
            break
    sum_ = to_plus + to_minus + 1
    for i2 in range(0, to_plus + 1):
        matrix[i][j + i2][1] = sum_
    for i2 in range(0, to_minus + 1):
        matrix[i][j - i2][1] = sum_
    return matrix

def main():
    H, W = map(int, input().split())
    matrix = []
    queue = deque()
    for i in range(0, H + 2):
        lines = []
        for j in range(0, W + 2):
            lines.append([-1, -1])
        matrix.append(lines)

    for i in range(1, H + 1):
        string = input()
        for j in range(1, W + 1):
            if string[j - 1] == "#":
                continue
            else:
                matrix[i][j] = [0, 0]
                queue.append([i, j])


    max_sum = 0
    while(queue):
        i, j = queue.pop()
        if (matrix[i][j][0] == 0):
            # y方向を埋める
            matrix = search_y(i, j, matrix)
        if (matrix[i][j][1] == 0):
            # x方向を埋める
            matrix = search_x(i, j, matrix)
        max_sum = max(matrix[i][j][0] + matrix[i][j][1], max_sum)
    
    print(max_sum - 1)



if __name__ == '__main__':
    main()