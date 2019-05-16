import numpy as np
import math
from collections import deque

def bfs(queue, adj_lists, n, colors):
    # 一つずつ入れていく
    now = 1
    queue.append(now)
    colors[1] = 0
    while(len(queue) != 0):
        now = queue[0]
        queue.popleft()
        potential_nexts = adj_lists[now]
        for next_ in potential_nexts:
            if colors[next_] != -1:
                continue
            else:
                queue.append(next_)
                colors[next_] = colors[now] + 1
    return colors



def main():
    n = int(input())
    adj_lists = {}
    colors = [-1] * (n + 1)
    for i in range(n):
        input_lists = [int(c) for c in input().split()]
        u = input_lists[0]
        d = input_lists[1]
        if (d == 0):
            adj_lists[u] = []
        else:
            adj_lists[u] = input_lists[2:]
    queue = deque()
    colors = bfs(queue, adj_lists, n, colors)
    for i in range(1, n + 1):
        print(str(i) + " " + str(colors[i]))


if __name__ == '__main__':
    main()