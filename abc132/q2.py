import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    n = int(input())
    P = [int(c) for c in input().split()]
    num = 0
    for i in range(1, n - 1):
        lists = [P[i - 1], P[i], P[i + 1]]
        max_ = max(lists)
        min_ = min(lists)
        if (P[i] != max_ and P[i] != min_):
            num += 1
    print(num)


if __name__ == '__main__':
    main()