import math

def main():
    N = int(input())
    lists = [int(c) for c in input().split()]
    assert(len(lists) == N)
    num = 0
    for i in range(N):
        j = N - 1
        while(j > i):
            if (lists[j - 1] > lists[j]):
                tmp = lists[j]
                lists[j] = lists[j - 1]
                lists[j - 1] = tmp
                num += 1
            j -= 1
    for i in range(N):
        print(lists[i], end="")
        if i != N-1:
            print(end=" ")
    print()
    print(num)


if __name__ == '__main__':
    main()