import math

def partition(S, left, right):
    norm = S[right]
    cnt = left
    wall = left
    for _ in range(left, right):
        if (S[cnt] > norm):
            cnt += 1
        else:
            tmp = S[cnt]
            S[cnt] = S[wall]
            S[wall] = tmp
            wall += 1
            cnt += 1
    # wallのところとnormを交換
    S[right] = S[wall]
    S[wall] = norm
    return S, wall


def quick_sort(n, S, left, right):
    S, mid = partition(S, left, right)
    if (mid - 1 - left > 0):
        S = quick_sort(n, S, left, mid - 1)
    if (right - mid - 1 > 0):
        S = quick_sort(n, S, mid + 1, right)
    return S




def main():
    n = int(input())
    S = [int(c) for c in input().split()]
    S = quick_sort(n, S, 0, n - 1)
    for i in range(len(S)):
        print(S[i], end="")
        if i != len(S) - 1:
            print(end=" ")
    print()


if __name__ == '__main__':
    main()