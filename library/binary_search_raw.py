import numpy as np
import math

def binary_search(x, S, left, right):
    # 要素xがSの中にあればTrue, なければFalseを返す
    if left > right:
        return False
    mid = (left + right) // 2
    if S[mid] == x:
        return True
    elif S[mid] > x:
        # もっと小さいところにある
        return binary_search(x, S, left, mid - 1)
    else:
        return binary_search(x, S, mid + 1, right)

def main():
    n = int(input())
    S = [int(i) for i in input().split()]
    q = int(input())
    T = [int(i) for i in input().split()]
    cnt = 0
    for i in range(q):
        if binary_search(T[i], S, 0, n - 1):
            cnt += 1
        else:
            pass
    
    print(cnt)


if __name__ == '__main__':
    main()