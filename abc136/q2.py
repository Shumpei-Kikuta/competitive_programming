import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    num = 0
    if 1 <= N and N <= 9:
        num = N
    elif 10 <= N and N <= 99:
        num = 9
    elif 100 <= N and N <= 999:
        num = N - 90
    elif 1000 <= N and N <= 9999:
        num = 909
    elif 10000 <= N and N <= 99999:
        num = N - 9090
    else:
        num = 90909
    print(num)


if __name__ == '__main__':
    main()