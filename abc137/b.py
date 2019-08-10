import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    K, X = map(int, input().split())
    for i in range(X - K + 1, K + X):
        print(i, end=" ")
    print()


if __name__ == '__main__':
    main()