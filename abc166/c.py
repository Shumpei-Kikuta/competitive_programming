import sys
sys.setrecursionlimit(10000000)


def main():
    N, M = map(int, input().split())
    H = [int(c) for c in input().split()]
    adj_lists = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        a, b = map(int, input().split())
        adj_lists[a].append(b)
        adj_lists[b].append(a)

    num = 0
    for k, v in adj_lists.items():
        flg = True
        for i in v:
            if H[k - 1] <= H[i - 1]:
                flg = False
                break
        if flg:
            num += 1
    print(num)



if __name__ == '__main__':
    main()
