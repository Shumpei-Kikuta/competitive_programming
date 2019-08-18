import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)
import heapq

def main():
    N = int(input())
    V = [int(c) for c in input().split()]
    heap = []
    for i in range(N):
        heapq.heappush(heap, V[i])

    for i in range(N -1 ):
        mini = heapq.heappop(heap)
        mini2 = heapq.heappop(heap)
        mean = (mini + mini2) / 2
        heapq.heappush(heap, mean)
    print(heap[0])



if __name__ == '__main__':
    main()