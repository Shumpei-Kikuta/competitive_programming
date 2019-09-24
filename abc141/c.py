import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N, K, Q = map(int, input().split())
    A = []
    points = []
    for _ in range(N):
        points.append(0)

    for _ in range(Q):
        winner = int(input())
        points[winner-1] += 1
    
    for i in points:
        if i > Q - K:
            print("Yes")
        else:
            print("No")

    


if __name__ == '__main__':
    main()