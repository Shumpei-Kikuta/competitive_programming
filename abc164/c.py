import sys
sys.setrecursionlimit(10000000)


def main():
    N = int(input())
    S = []
    sets = set()
    for i in range(N):
        sets.add(input())
    print(len(sets))
    



if __name__ == '__main__':
    main()
