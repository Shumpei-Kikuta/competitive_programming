import sys
sys.setrecursionlimit(10000000)
import numpy as np


def main():
    R = int(input())
    print(np.pi * 2 * R)


if __name__ == '__main__':
    main()
