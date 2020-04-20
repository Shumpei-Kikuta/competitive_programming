import sys
sys.setrecursionlimit(10000000)
import numpy as np


def rec(dp, S, A, i):
    if i == len(dp):
        return 0
    for u in range(len(dp)):
        if dp[u] == 1:
            continue
        else:
            dp[S] = max(rec(np.append(dp[S], u), S.add(u), A, i + 1) + A[u] * abs(u - i))


def main():
    N = int(input())
    A = [int(c) for c in input().split()]

    dp = np.array([0] * N)
    rec(dp, set(), A, 0)





if __name__ == '__main__':
    main()
