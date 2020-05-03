import sys
sys.setrecursionlimit(10000000)


def main():
    N, K = map(int, input().split())
    nums = [0] * N
    for i in range(K):
        _ = int(input())
        A = [int(c) for c in input().split()]
        for a in A:
            nums[a-1] += 1

    num = 0
    for i in range(N):
        if nums[i] == 0:
            num += 1

    print(num)


if __name__ == '__main__':
    main()
