import sys
sys.setrecursionlimit(10000000)


def main():
    N = int(input())
    A = [int(c) for c in input().split()]

    r = 0
    dicts = {i: 0 for i in range(1, 10**5 + 1)}
    dicts[A[r]] += 1
    max_num = 1
    for l in range(N):
        while(r < N - 1 and dicts[A[r+1]] == 0):
            dicts[A[r+1]] += 1
            r += 1
        max_num = max(max_num, r - l + 1)
        dicts[A[l]] -= 1
        if r == l:
            r += 1
            if r < N:
                dicts[A[r]] += 1
    print(max_num)


if __name__ == '__main__':
    main()
