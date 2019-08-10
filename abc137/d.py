import numpy as np
import math
import sys
import heapq
sys.setrecursionlimit(10000000)

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
    
    AB = sorted(AB)
    ans = 0
    idx = 0
    priority_queue = []
    for i in range(1, M + 1):
        # print(i)
        while True:
            if idx < N and AB[idx][0] <= i:
                heapq.heappush(priority_queue, - AB[idx][1])
                idx += 1
            else:
                break
        if len(priority_queue) == 0:
            continue
        else:
            max_element = - heapq.heappop(priority_queue)
            ans += max_element
    print(ans)



if __name__ == '__main__':
    main()