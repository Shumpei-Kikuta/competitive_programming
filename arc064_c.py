import sys
sys.setrecursionlimit(10000000)


def main():
    N, x = map(int, input().split())
    A = [int(c) for c in input().split()]

    num = 0
    if A[0] > x:
        num += A[0] - x
        A[0] = x
    for i in range(1, N):
        if A[i - 1] + A[i] > x:
            num += A[i] + A[i - 1] - x
            A[i] = x - A[i - 1]
    print(num)
            


if __name__ == '__main__':
    main()
