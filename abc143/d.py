import bisect

def main():
    N = int(input())
    L = [int(i) for i in input().split()]
    L.sort()
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            k = bisect.bisect_left(L, L[i] + L[j])
            k -= 1
            count += k - j
    print(count)


if __name__ == "__main__":
    main()