import math
import sys
sys.setrecursionlimit(10000000)

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = None

def unite(x: Node, y: Node, nodes):
    """xを含む集合とyを含む集合を併合"""
    x_root, x_depth = root(x, 0)
    y_root, y_depth = root(y, 0)

    # xの根を併合後の根とする
    if y_root != x_root:
        if x_depth >= y_depth:
            y_root.parent = x_root
            nodes[y_root.idx] = y_root
        else:
            x_root.parent = y_root
            nodes[x_root.idx] = x_root
    return nodes


def same(x: Node, y: Node):
    """xとyが同じ集合に所属するか？すれば1, しなければ0を返す"""
    x_root, _ = root(x, 0)
    y_root, _ = root(y, 0)
    if x_root.idx == y_root.idx:
        return 1
    else:
        return 0

def root(x: Node, cnt: int):
    """Node xの所属する木の根を探索"""
    if x.parent is None:
        return x, cnt
    else:
        return root(x.parent, cnt + 1)

def main():
    n, q = map(int, input().split())
    nodes = []
    for i in range(n):
        node = Node(i)
        nodes.append(node)

    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            # unite x and y
            nodes = unite(nodes[x], nodes[y], nodes)
        else:
            # is x and y belonging the same tree
            print(same(nodes[x], nodes[y]))


    


if __name__ == '__main__':
    main()