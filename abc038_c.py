import sys
sys.setrecursionlimit(10000000)


def main():
    N = int(input())
    A = [int(c) for c in input().split()]
    left = 0
    right = 0
    num = 0
    while(right < N):
        while(right + 1 < N):
            if A[right + 1] > A[right]:
                right += 1
            else:
                break
        for i in range(1, right - left + 1):
            num += i
        right += 1
        left = right
    num += N
    print(num)


if __name__ == '__main__':
    main()
