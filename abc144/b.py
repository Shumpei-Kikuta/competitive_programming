import sys
sys.setrecursionlimit(10000000)


def main():
    N = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if N == i * j:
                print("Yes")
                sys.exit()
    print("No")

if __name__ == '__main__':
    main()
