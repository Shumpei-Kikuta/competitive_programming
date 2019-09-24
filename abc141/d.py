import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)
import heapq


def main():
    N, M = map(int, input().split())
    A = [int(c) for c in input().split()]
    queue = []

    for i in range(N):
        heapq.heappush(queue, - A[i])
    for i in range(M):
        max_ = heapq.heappop(queue)
        heapq.heappush(queue, int(max_/2))
    
    print(- sum(queue))


if __name__ == '__main__':
    main()