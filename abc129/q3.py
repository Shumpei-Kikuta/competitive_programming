import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N, M = map(int, input().split())
    A = [0] * (N + 1)
    for i in range(M):
        bre = int(input())
        A[bre] = -1
    a_2 = 1
    a_1 = 1 if A[1] != -1 else -1
    # print(A)
    for i in range(N):
        if (A[i] == -1) & (A[i + 1] == -1):
            print(0)
            sys.exit()
    # print(a_1, a_2)
    A[0] = 1
    A[1] = 1 if A[1] != -1 else -1
    for i in range(2, N + 1):
        if A[i] == -1:
            a_2 = a_1
            a_1 = -1
            continue
        elif a_1 == -1:
            a = a_2
        elif a_2 == -1:
            a = a_1
        else:
            a = a_1 +a_2
        a_2 = a_1
        a_1 = a
        # print(a_2, a_1)
    print(a % 1000000007)

if __name__ == '__main__':
    main()