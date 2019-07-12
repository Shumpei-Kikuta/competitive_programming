import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N, K = map(int, input().split())
    A = [int(c) for c in input().split()]
    left = 0
    right = 1
    num = 0
    cumsum = [0] * (N + 1)
    cumsum[0] = 0
    for i in range(1, N + 1):
        cumsum[i] = cumsum[i - 1] + A[i - 1]
    while(right <= N):
        # print(sum(A[left:right]))
        if cumsum[right] - cumsum[left] >= K:
            num += N - right + 1
            left += 1
        else:
            right += 1 
    print(num)


if __name__ == '__main__':
    main()