import sys
sys.setrecursionlimit(10000000)


def main():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(int(input()))

    for i in range(N):
        if S[i] == 0:
            print(N)
            sys.exit()
    
    left, right = 0, 0
    max_len = 0
    num = 1
    while(right < N):
        if num * S[right] <= K:
            # right update
            max_len = max(max_len, right - left + 1)
            if right + 1 == N:
                break
            num *= S[right]
            right += 1
        else:
            # left update
            if left == right:
                if right + 1 == N:
                    break
                left += 1
                right += 1
                num = S[left]
            else:
                num /= S[left]
                left += 1
    print(max_len)


if __name__ == '__main__':
    main()
