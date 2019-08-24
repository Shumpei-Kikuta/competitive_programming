import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    M, D = map(int, input().split())
    num = 0
    for m in range(1, M + 1):
        for d in range(1, D + 1):
            if d <= 21:
                continue
            else:
                d1 = d % 10
                d2 = (d - d1) // 10
                if d1 < 2:
                    continue
                if d2 < 2:
                    continue
                if d1 * d2 == m:
                    num += 1
    print(num)



if __name__ == '__main__':
    main()