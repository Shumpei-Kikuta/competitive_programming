import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    H = [int(c) for c in input().split()]
    for i in range(N - 1):
        if (H[i] > H[i + 1]):
            print("No")
            sys.exit()
        elif (H[i] == H[i + 1]):
            continue
        else:
            H[i + 1] -= 1
    print("Yes")

if __name__ == '__main__':
    main()