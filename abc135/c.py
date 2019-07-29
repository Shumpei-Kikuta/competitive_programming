import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    A = [int(c) for c in input().split()]
    B = [int(c) for c in input().split()]
    cnt = 0
    for i in range(N):
        each_cnt = min(A[i], B[i])
        A[i] -= each_cnt
        B[i] -= each_cnt
        cnt += each_cnt
        if B[i] != 0:
            each_cnt = min(A[i + 1], B[i])
            A[i + 1] -= each_cnt
            B[i] -= each_cnt
            cnt += each_cnt
        else:
            continue
    print(cnt)
            


if __name__ == '__main__':
    main()