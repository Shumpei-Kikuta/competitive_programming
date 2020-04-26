import sys
sys.setrecursionlimit(10000000)


def main():
    S, W = map(int, input().split())
    if W >= S:
        print('unsafe')
    else:
        print('safe')


if __name__ == '__main__':
    main()
