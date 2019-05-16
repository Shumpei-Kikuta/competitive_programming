import math

def dfs(adj_lists, n, node, time, time_lists):
    # あるノードにいるとき．
    potential_nexts = adj_lists[node]
    for i in range(1, n + 1):
        if (i in potential_nexts) and (time_lists[i][0] == 0):
            # 隣接していてまだ，言ったことがないところ
            time += 1
            time_lists[i][0] = time
            time, time_lists = dfs(adj_lists, n, i, time, time_lists)
    time += 1
    time_lists[node][1] = time
    return time, time_lists


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

    time_lists[1][0] = 1
    time = 1
    time, time_lists = dfs(adj_lists, n, 1, time, time_lists)
    for i in range(1, n + 1):
        if (time_lists[i][0] == 0):
            time += 1
            time_lists[i][0] = time
            dfs(adj_lists, n, i, time, time_lists)
    for i in range(1, n + 1):
        print(str(i) + " " + str(time_lists[i][0]) + " " + str(time_lists[i][1]))



if __name__ == '__main__':
    main()