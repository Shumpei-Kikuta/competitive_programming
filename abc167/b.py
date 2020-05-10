import sys
sys.setrecursionlimit(10000000)


def main():
    A, B, C, K = map(int, input().split())
    num = K
    if K <= A:
        print(K)
    elif (A + B) >= K:
        print(A)
    else:
        # import pdb; pdb.set_trace()
        print(2 * A + B - K)


if __name__ == '__main__':
    main()
