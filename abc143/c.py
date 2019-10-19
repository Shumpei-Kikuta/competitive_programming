import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    S = input()

    num = 1
    for i in range(1, N):
        if S[i] != S[i - 1]:
            num += 1
    print(num)

if __name__ == '__main__':
    main()