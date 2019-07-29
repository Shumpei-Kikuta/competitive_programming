import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    P = [int(c) for c in input().split()]
    sorted_P = sorted(P)
    if sorted_P == P:
        print("YES")
        sys.exit()
    for i in range(N):
        for j in range(N):
            copied_P = P.copy()
            if i == j:
                continue
            tmp = copied_P[i]
            copied_P[i] = copied_P[j]
            copied_P[j] = tmp
            if sorted_P == copied_P:
                print("YES")
                sys.exit()
                break
            else:
                continue
    else:
        print("NO")
            


if __name__ == '__main__':
    main()