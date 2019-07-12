import numpy as np
import math
from stack import Stack

# class Graph():
#     def __init__(self):

def dfs(stack, adj_lists, time_lists, time, n):
    # stackに状態を格納しながら，探索を行う
    now = min(adj_lists)
    time += 1
    stack.append(now)
    time_lists[now][0] = 1

    while(len(stack) > 0):
        time += 1
        potential_nexts = adj_lists[now]
        for i in range(1, n + 1):
            if (i in potential_nexts) and (time_lists[i][0] == 0):
                now = i
                stack.append(now)
                time_lists[i][0] = time
                break
        else:
            now = stack[-1]
            stack.pop()
            time_lists[now][1] = time
        print(time_lists)
        print(now)




def main():
    adj_lists = {}
    n = int(input())
    time_lists = {}
    for i in range(n):
        input_list = [int(c) for c in input().split()]
        u = input_list[0]
        v = input_list[2:]
        adj_lists[u] = v
        time_lists[u] = [0, 0]

    stack = []
    time = 0
    dfs(stack, adj_lists, time_lists, time, n)


if __name__ == '__main__':
    main()