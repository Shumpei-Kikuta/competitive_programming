import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    A, B, C = [int(c) for c in input().split()]
    if (A - B) < C:
        C -= (A - B)
    else:
        C = 0
    print(C)


if __name__ == '__main__':
    main()