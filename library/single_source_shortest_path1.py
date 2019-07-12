import math
INF = 1000001

def dijkstra(adj_matrix, colors, n, distance):
    """最短距離を計算する
    一つずつ，距離を確定して行く
    """
    now = 0
    while(True):
        # 全てのcolorが1になったらbreak
        if (sum(colors) == n):
            break
        # まず，距離を更新
        min_distance = INF
        min_node = n
        for i in range(n):
            if colors[i] == 1:
                continue
            distance[i] = min(distance[now] + adj_matrix[now][i], distance[i])
            if distance[i] < min_distance:
                min_distance = distance[i]
                min_node = i    
        # nowの隣接ノードで一番小さいところを探し，colorを1にする，
        colors[min_node] = 1
        # nowを移動
        now = min_node
    return distance
        





def main():
    n = int(input())
    adj_matrix = []
    colors = [0] * n
    distance = [INF] * n
    for i in range(n):
        adj_matrix.append([INF] * n)
    for i in range(n):
        input_lists = [int(c) for c in input().split()]
        u = input_lists[0]
        d = input_lists[1]
        for j in range(d):
            v = input_lists[2 * j + 2]
            adj_matrix[i][v] = input_lists[2 * j + 3]
    colors[0] = 1
    distance[0] = 0
    distance = dijkstra(adj_matrix, colors, n, distance)

    for i in range(n):
        print(str(i) + " " + str(distance[i]))

if __name__ == '__main__':
    main()