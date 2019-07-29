import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    A, B = map(int, input().split())
    K = (A + B) / 2
    if math.ceil(K) != K:
        print("IMPOSSIBLE")
    else:
        print(int(K))

if __name__ == '__main__':
    main()