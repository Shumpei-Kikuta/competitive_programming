import sys
sys.setrecursionlimit(10000000)


def main():
    N, K = map(int, input().split())
    A = [0]
    B = [int(c) for c in input().split()]
    A.extend(B)
    dicts = {i: 0 for i in range(1, N + 1)}

    now = 1
    dicts[now] = 0
    num = 0
    flag = False
    while(num < K):
        now = A[now]
        num += 1
        if dicts[now] == 0:
            dicts[now] = num
            continue
        elif not flag:
            cycle = num - dicts[now]
            left = (K - num) % cycle
            K = left
            num = 0
            flag = True
    print(now)







if __name__ == '__main__':
    main()
