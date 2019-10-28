import sys
sys.setrecursionlimit(10000000)


def main():
    N = int(input())
    min_ = N - 1
    for i in range(1, int(N ** 0.5) + 1):
        if N % i != 0:
            continue
        else:
            j = N // i
            min_ = min(min_, i + j - 2)
    print(min_)


if __name__ == '__main__':
    main()
