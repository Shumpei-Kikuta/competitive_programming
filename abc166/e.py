import sys
sys.setrecursionlimit(10000000)


def main():
    N = int(input())
    A = [int(c) for c in input().split()]

    # 自分が1だったときのそれ以降
    lists = [0] * (N + 1)
    for i, a in enumerate(A):
        if i <= a:
            continue
        lists[i + 1 - a] += 1
    
    num = 0
    for i, a in enumerate(A):
        idx = i + 1
        if idx + a <= N:
            num += lists[idx + a]
    print(num)







if __name__ == '__main__':
    main()
