import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

INF = 100000000

def main():
    N, L = map(int, input().split())
    apples = [i for i in range(L, L + N)]
    sum_ = sum(apples)
    without_self_sum = [sum_ - apples[i] for i in range(N)]
    abs_minimum = INF
    ans = 0
    for i in range(N):
        if abs(sum_ - without_self_sum[i]) < abs_minimum:
            abs_minimum = abs(sum_ - without_self_sum[i])
            ans = without_self_sum[i]
    print(ans)

if __name__ == '__main__':
    main()