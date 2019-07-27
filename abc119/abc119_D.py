import numpy as np
import math
import sys
import bisect
sys.setrecursionlimit(10000000)
INF = 1e11

def main():
    # 入力処理
    A, B, Q = [int(c) for c in input().split()]
    S = []
    T = []
    X = []
    for i in range(A):
        S.append(int(input()))
    for i in range(B):
        T.append(int(input()))
    for i in range(Q):
        X.append(int(input()))
    S.append(INF)
    T.append(INF)

    for i, x in enumerate(X):
        # s -> t
        sa = bisect.bisect_left(S, x) - 1
        sb = sa + 1

        # t -> s
        tc = bisect.bisect_left(T, x) - 1
        td = tc + 1
        distance = INF
        for s in [sa, sb]:
            for t in [tc, td]:
                dis1 = abs(x - S[s]) + abs(S[s] - T[t])
                dis2 = abs(x - T[t]) + abs(T[t] - S[s])
                distance = min(dis1, dis2, distance)
        print(distance)



if __name__ == '__main__':
    main()