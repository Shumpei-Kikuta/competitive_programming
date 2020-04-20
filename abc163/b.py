import sys
sys.setrecursionlimit(10000000)


def main():
    N, M = map(int, input().split())
    A = [int(c) for c in input().split()]
    import numpy as np
    sum_ = np.sum(A)
    if N - sum_ < 0:
        print(-1)
    else:
        print(N - sum_)


if __name__ == '__main__':
    main()

