import numpy as np
import math

INF = 1000000000000
count__ = 0

def merge(n, S, left, mid, right):
    L = [S[i] for i in range(left, mid + 1)] #size = mid - left + 1
    R = [S[i] for i in range(mid + 1, right + 1)] #size = right - mid
    l = 0
    r = 0
    L.append(INF)
    R.append(INF)
    cnt = 0
    while(cnt < right - left + 1):
        if (L[l] < R[r]):
            S[cnt + left] = L[l]
            l += 1
        else:
            S[cnt + left] = R[r]
            r += 1
        cnt += 1
        global count__
        count__ += 1
    return S

def merge_sort(n: int, S: list, left: int, right: int):
    if (left == right):
        pass
    else:
        mid = (left + right) // 2
        merge_sort(n, S, left, mid)
        merge_sort(n, S, mid + 1, right)
        S = merge(n, S, left, mid, right)
    return S

def main():
    n = int(input())
    S = [int(c) for c in input().split()]
    S = merge_sort(n, S, 0, n - 1)
    for i in range(len(S)):
        print(S[i], end="")
        if i != len(S) - 1:
            print(end=" ")
    print()
    print(count__)


if __name__ == '__main__':
    main()