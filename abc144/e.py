import sys
sys.setrecursionlimit(10000000)
import heapq
import math

def main():
    N, K = map(int, input().split())
    A = [int(c) for c in input().split()]
    F = [int(c) for c in input().split()]
    
    A.sort()
    F.sort(reverse=True)

    num = 0
    sum_ = []
    for i in range(len(A)):
        sum_.append(A[i] * F[i])
    left = 0
    right = 10 ** 12
    while(num < 50):
        number = 0
        mid = (left + right) // 2
        # print(mid)
        for i in range(len(A)):
            if sum_[i] <= mid:
                continue
            else:
                number += math.ceil((sum_[i] - mid) / F[i])
            # print(number)
        if number > K:
            # 最大値をmidより小さくできない -> 最大値はもっとでかい
            left = mid + 1
        else:
            right = mid
        num += 1
    print(mid)
                

if __name__ == '__main__':
    main()
