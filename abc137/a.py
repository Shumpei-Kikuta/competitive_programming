import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    A, B = map(int, input().split())
    print(max(A + B, A - B, A * B))


if __name__ == '__main__':
    main()