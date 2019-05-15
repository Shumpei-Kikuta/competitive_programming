import math
import sys

class Node():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Dubbly_linked_list():
    def __init__(self):
        # null を作る
        self.nil = Node(None)
        self.nil.left = self.nil
        self.nil.right = self.nil
    
    def insert(self, x):
        # 先頭にxをkeyとしたノードを挿入
        node = Node(x)
        node.right = self.nil.right
        self.nil.right.left = node
        node.left = self.nil
        self.nil.right = node

    def __search_x(self, x):
        # xを持つ最初のノードを返す
        cursor = self.nil.right
        while(cursor != self.nil):
            if cursor.value == x:
                return cursor
            else:
                cursor = cursor.right
        return None
    
    def delete(self, x):
        # xをkeyとした最初のノードの削除
        delNode = self.__search_x(x)
        if delNode is None:
            print("error: There's no value having {}".format(x))
            sys.exit()
        else:
            delNode.right.left = delNode.left
            delNode.left.right = delNode.right

    def deleteFirst(self):
        # 先頭のノードを削除
        if self.nil.right == self.nil:
            print("error: only nil has existed")
            sys.exit()
        else:
            delNode = self.nil.right
            delNode.right.left = delNode.left
            delNode.left.right = delNode.right
    def deleteLast(self):
        if self.nil.left == self.nil:
            print("error: only nil has existed")
            sys.exit()
        else:
            delNode = self.nil.left
            delNode.right.left = delNode.left
            delNode.left.right = delNode.right
    
    def print(self):
        # 全ての要素をprintする
        cursor = self.nil.right 
        while(cursor != self.nil):
            print(cursor.value, end="")
            cursor = cursor.right
            if cursor != self.nil:
                print(end=" ")
        print()


def main():
    DLL = Dubbly_linked_list()
    n = int(input())
    for _ in range(n):
        command = input()
        if command[6] == "F":
            DLL.deleteFirst()
        elif command[6] == 'L':
            DLL.deleteLast()
        else:
            command, x = command.split()
            x = int(x)
            if command[0] == "i":
                DLL.insert(x)
            else:
                DLL.delete(x)
 
    DLL.print()




if __name__ == '__main__':
    main()