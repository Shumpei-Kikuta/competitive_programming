import sys
sys.setrecursionlimit(10000000)


def main():
    A, B, C, D = map(int, input().split())
    while(True):
        C = C - B
        if C <= 0:
            print('Yes')
            break
        A = A - D
        if A <= 0:
            print('No')
            break


if __name__ == '__main__':
    main()
