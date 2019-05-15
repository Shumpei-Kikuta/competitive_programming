import math

class Node():
    def __init__(self, parent=None, left=None, right=None, value=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value

class BinarySearchTree():
    def __init__(self):
        self.nil = Node()
        self.nil.parent = self.nil
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.root = self.nil

    def find(self, x: int):
        # xというkeyを探索する
        now = self.root
        while(now != self.nil):
            if (now.value == x):
                return True
            elif (now.value > x):
                # xは左側
                now = now.left
            else:
                now = now.right
        return False

    def insert(self, x: int):
        # int xというvalueをもったノードをどこに挿入するか
        now = self.nil.right #初期化
        node = Node(None, self.nil, self.nil, value=x)
        if now.value is None:
            self.nil.left = node
            self.nil.right = node
            now.parent = self.nil
            self.root = node
            self.root.parent = self.nil
        else:
            now = self.root
            while(True):
                if now.value <= node.value:
                    if now.right != self.nil:
                        now = now.right
                    else:
                        now.right = node
                        node.parent = now
                        break
                elif now.value > node.value:
                    if now.left != self.nil:
                        now = now.left
                    else:
                        now.left = node
                        node.parent = now
                        break
        # print("node:", node.value)
        # print("parent: ", node.parent.value)

    def __preorder(self, node):
        # preorderで出力
        print(end=" ")
        print(node.value, end="")
        if (node.left != self.nil):
            self.__preorder(node.left)
        if (node.right != self.nil):
            self.__preorder(node.right)


    def __inorder(self, node):
        # inorderで質力
        if (node.left != self.nil):
            self.__inorder(node.left)
        print(end=" ")
        print(node.value, end="")
        if (node.right != self.nil):
            self.__inorder(node.right)

    def print(self):
        # inorder, preorderで出力
        self.__inorder(self.root)
        print()
        self.__preorder(self.root)
        print()

    def __search(self, x):
        now = self.root
        while(now != self.nil):
            if (now.value == x):
                return now
            elif (now.value > x):
                # xは左側
                now = now.left
            else:
                now = now.right
        return self.nil

    def __get_next_node(self, node):
        next_node = node.left
        while(True):
            if (next_node.left != self.nil):
                next_node = next_node.left
            else:
                break
        return next_node

    def __delete_node(self, node):
        if (node.left == self.nil) & (node.right == self.nil):
            # 子がいない時
            if (node.parent.left == node):
                # node が左の子の時
                node.parent.left = self.nil
            else:
                node.parent.right = self.nil
        elif (node.left != self.nil) & (node.right != self.nil):
            #子がふたついる時
            # 次の接点を求める
            next_node = self.__get_next_node(node.right)
            self.__delete_node(next_node)
            node.value = next_node.value
        else:
            # 子が一つの時
            if (node.parent.left == node):
                #  nodeが左の子の時
                if (node.left != self.nil):
                    # nodeは左に子を持っている
                    node.parent.left = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.left = node.right
                    node.right.parent = node.parent
            else:
                # nodeは右の子
                if node.left != self.nil:
                    # nodeは左に子を持つ
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent
        del node

    def delete(self, x):
        # xのkeyを持つ奴を削除する
        node = self.__search(x)
        if (node == self.nil):
            pass
        else:
            self.__delete_node(node)


        


def main():
    n = int(input())
    bst = BinarySearchTree()
    for i in range(n):
        command = input()
        if command[0] == "p":
            bst.print()
        elif command[0] == "i":
            command, k = command.split()
            k = int(k)
            bst.insert(k)
        elif command[0] == "f":
            command, k = command.split()
            k = int(k)
            if bst.find(k):
                print("yes")
            else:
                print("no")
        elif command[0] == "d":
            command, k = command.split()
            k = int(k)
            bst.delete(k)

if __name__ == '__main__':
    main()