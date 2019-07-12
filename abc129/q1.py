import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    P, Q, R = map(int, input().split())
    lists = []
    lists.append(P + Q)
    lists.append(Q + R)
    lists.append(P + R)
    print(min(lists))


if __name__ == '__main__':
    main()