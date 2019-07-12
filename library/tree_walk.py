
import math

class Node():
    def __init__(self, id_: int, left: int, right: int, parent: int):
        self.id_ = id_
        self.left = left
        self.right = right
        self.parent = parent

def get_top(node_lists: list) -> Node:
    # node_listsの中からrootを返す．
    for i in range(len(node_lists)):
        if node_lists[i].parent == -1:
            return node_lists[i]


def preorder(node, node_lists):
    # preorder巡回，root, 左，右の順番
    print(" " + str(node.id_), end="")
    if node.left != -1:
        preorder(node_lists[node.left], node_lists)
    if node.right != -1:
        preorder(node_lists[node.right], node_lists)


def inorder(node, node_lists):
    # inorder巡回、左，root，右の順番
    if node.left != -1:
        inorder(node_lists[node.left], node_lists)
    print(" " + str(node.id_), end="")
    if node.right != -1:
        inorder(node_lists[node.right], node_lists)

def postorder(node, node_lists):
    # postorder巡回，左，右，root
    if node.left != -1:
        postorder(node_lists[node.left], node_lists)
    if node.right != -1:
        postorder(node_lists[node.right], node_lists)
    print(" " + str(node.id_), end="")

def main():
    n = int(input())
    node_lists = []
    for i in range(n):
        node = Node(-1, -1, -1, -1)
        node_lists.append(node)

    for i in range(n):
        id_, left, right = [int(i) for i in input().split()]
        node_lists[id_].id_ = id_
        node_lists[id_].left = left
        node_lists[id_].right = right
        if right != -1:
            node_lists[right].parent = id_
        if left != -1:
            node_lists[left].parent = id_
  
    top = get_top(node_lists)
    print("Preorder")
    preorder(top, node_lists)
    print()
    print("Inorder")
    inorder(top, node_lists)
    print()
    print("Postorder")
    postorder(top, node_lists)
    print()
    



if __name__ == '__main__':
    main()