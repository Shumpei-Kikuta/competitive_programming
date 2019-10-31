import sys
sys.setrecursionlimit(10000000)


def main():
    N = int(input())
    A = [int(c) for c in input().split()]
    l = 0
    r = 0
    num = 0
    while(r < N):
        while(r + 1 < N):
            if A[r + 1] > A[r]:
                r += 1
            else:
                break
        for i in range(1, r - l + 1):
            num += i
        r += 1
        l = r
    num += N
    print(num)
            

if __name__ == '__main__':
    main()
