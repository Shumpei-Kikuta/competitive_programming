import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    D = [int(c) for c in input().split()]
    sorted_D = sorted(D)
    upper = sorted_D[N//2]
    lower = sorted_D[N//2 - 1]
    print(upper - lower)


if __name__ == '__main__':
    main()