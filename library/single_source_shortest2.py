import math
from priority_queue import PriorityQueue

INF = 1000001

def dijkstra(adj_lists, n, distance, colors):
    # 優先度付きQueueを用いる
    # まず，nowを格納し，初期化
    now = 1
    distance[0] = 0
    colors[0] = 1
    # Priority queueを初期化，nowに隣接した奴らのdistanceをqueueへ入れる
    pqueue = PriorityQueue()
    for i in range(len(adj_lists[now])):
        pqueue.insert()
    # numがnになるまで
    while(num < n):
        num += 1

def main():
    n = int(input())
    adj_lists = {}
    colors = [0] * n
    distance = [INF] * n
    for i in range(n):
        adj_lists[i] = []
    for i in range(n):
        input_lists = [int(c) for c in input().split()]
        u = input_lists[0]
        d = input_lists[1]
        lists = []
        for j in range(d):
            v = input_lists[2 * j + 2]
            lists.append([v, input_lists[2 * j + 3]])
        adj_lists[i] = lists
    assert(len(adj_lists) == n)
    dijkstra(adj_lists, n, distance, colors)

if __name__ == '__main__':
    main()