import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    W = [int(c) for c in input().split()]
    dis = 100000000000
    for i in range(1, N):
        S1 = W[:i]
        S2 = W[i:]
        # print(S1, S2)
        dis = min(dis, abs(sum(S1)-sum(S2)))
    print(dis)


if __name__ == '__main__':
    main()