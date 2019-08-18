import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    A = [int(c) for c in input().split()]
    num = 0
    for i in range(N):
        num += 1 / A[i]
    print(1/num)


if __name__ == '__main__':
    main()