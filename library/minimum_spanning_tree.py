import math
INF = 3000

def minimum_spanning(w, colors, adj_matrix, num):
    """
    重みの総和を返す．
    colorsが1のものと繋がっているリンクのうち，一番小さいものを選ぶ
    """
    n = len(colors)
    if num < n:
        minimum_edge = INF
        minumum_node = n
        for i in range(n):
            if colors[i] == 1:
                for j in range(n):
                    if colors[j] == 0:
                        if (adj_matrix[i][j] < minimum_edge):
                            minimum_edge = adj_matrix[i][j]
                            minimum_node = j
        w += minimum_edge
        colors[minimum_node] = 1
        return minimum_spanning(w, colors, adj_matrix, num + 1)
    else:
        return w

def main():
    n = int(input())
    adj_matrix = []
    for i in range(n):
        input_lists = [int(c) for c in input().split()]
        for i in range(n):
            if input_lists[i] == -1:
                input_lists[i] = INF
        adj_matrix.append(input_lists)
    assert(len(adj_matrix) == n)
    w = 0
    colors = [0] * n
    colors[0] = 1
    w = minimum_spanning(w, colors, adj_matrix, 1)
    print(w)


if __name__ == '__main__':
    main()