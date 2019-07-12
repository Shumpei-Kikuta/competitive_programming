#include <iostream>
#include <algorithm>
using namespace std;

int N;
int main(){

    N = int(input())
    adj_lists = {}
    for i in range(1, N + 1):
        adj_lists[i] = []
    nodes = [-1] * (N + 1)
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adj_lists[u].append((v, w))
        adj_lists[v].append((u, w))
    nodes[1] = 1
    nodes = dfs(adj_lists, nodes, 1)
    ans = nodes[1:]
    for color in ans:
        print(color)
    return 0;
}

def contrary_bit(bit):
    if (bit == 1):
        return 0
    elif (bit == 0):
        return 1
    else:
        print("error")

def dfs(adj_lists, nodes, node):
    # nodeから出発して，深さ優先探索
    neighbors = adj_lists[node]
    for neighbor in neighbors:
        if (nodes[neighbor[0]] != -1):
            #訪問済み
            continue
        else:
            if neighbor[1] % 2 == 0:
                # 同じbit  
                nodes[neighbor[0]] = nodes[node]
                nodes = dfs(adj_lists, nodes, neighbor[0])
            else:
                nodes[neighbor[0]] = contrary_bit(nodes[node])
                nodes = dfs(adj_lists, nodes, neighbor[0])
    return nodes

def main():
    N = int(input())
    adj_lists = {}
    for i in range(1, N + 1):
        adj_lists[i] = []
    nodes = [-1] * (N + 1)
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adj_lists[u].append((v, w))
        adj_lists[v].append((u, w))
    nodes[1] = 1
    nodes = dfs(adj_lists, nodes, 1)
    ans = nodes[1:]
    for color in ans:
        print(color)

if __name__ == '__main__':
    main()