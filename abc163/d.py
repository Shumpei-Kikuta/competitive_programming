import sys
sys.setrecursionlimit(10000000)


def main():
    N, K = map(int, input().split())

    num = 0
    min_sum = sum(range(0, K))
    max_sum = sum(range(N + 1 - K ,N + 1))

    for i in range(N + 2 - K):
        num += max_sum - min_sum + 1
        max_sum += N - K - i
        min_sum += K + i

    D = 10 ** 9 + 7
    print(num % D)



if __name__ == '__main__':
    main()
