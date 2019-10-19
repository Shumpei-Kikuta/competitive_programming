import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    D = [int(c) for c in input().split()]
    num = 0
    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            num += D[i] * D[j]
    print(num)
    
            
        


if __name__ == '__main__':
    main()