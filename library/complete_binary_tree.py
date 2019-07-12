import math

def main():
    H = int(input())
    nodes = [] * (H + 1)
    nodes.append(0)
    input_list = [int(c) for c in input().split()]
    nodes += input_list
    
    for i in range(1, H + 1):
        print("node {0}: key = {1},".format(i, nodes[i]), end=" ")
        if i != 1:
            print("parent key = {},".format(nodes[int(i / 2)]), end=" ")
        if i * 2 <= H:
            print("left key = {},".format(nodes[int(2 * i)]), end=" ")
        if (i * 2 + 1) <= H:
            print("right key = {},".format(nodes[int(2 * i + 1)]), end=" ")
        print()

if __name__ == '__main__':
    main()