import math

time = 1
time_lists = {}
def dfs(adj_lists, n, node):
    # あるノードにいるとき．
    potential_nexts = adj_lists[node]
    flag = False
    global time_lists
    global time
    for i in range(1, n + 1):
        if (i in potential_nexts) and (time_lists[i][0] == 0):
            # 隣接していてまだ，言ったことがないところ
            time += 1
            time_lists[i][0] = time
            dfs(adj_lists, n, i)
    time += 1
    time_lists[node][1] = time


def main():
    adj_lists = {}
    n = int(input())
    for i in range(n):
        input_list = [int(c) for c in input().split()]
        u = input_list[0]
        v = input_list[2:]
        adj_lists[u] = v
        global time_lists
        time_lists[u] = [0, 0]

    time_lists[1][0] = 1
    dfs(adj_lists, n, 1)
    for i in range(1, n + 1):
        if (time_lists[i][0] == 0):
            global time
            time += 1
            time_lists[i][0] = time
            dfs(adj_lists, n, i)
    for i in range(1, n + 1):
        print(str(i) + " " + str(time_lists[i][0]) + " " + str(time_lists[i][1]))



if __name__ == '__main__':
    main()