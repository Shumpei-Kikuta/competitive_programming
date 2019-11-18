import sys
sys.setrecursionlimit(10000000)

INF = 1000000


def main():
    H, W = map(int, input().split())
    adj_matrix = [[int(c) for c in input().split()] for i in range(10)]

    A = [[int(c) for c in input().split()] for i in range(H)]

    def solve(now, S, dp):
        if now == 1:
            dp[now][S] = 0
            return dp[now][S]
        elif dp[now][S] != INF:
            # 訪問済み
            return dp[now][S]
        else:
            res = INF
            for i in range(10):
                if i == now:
                    continue
                if not (S >> i & 1):
                    res = min(res, solve(i, S | (1 << i), dp) + adj_matrix[now][i])
            dp[now][S] = res
            return dp[now][S]

    minimum_distance = {}
    for i in range(10):
        dp = [[INF for c in range(1 << 10)] for i in range(10)]
        minimum_distance[i] = solve(i, 1 << i, dp)

    wall_num = {i: 0 for i in range(10)}
    for line_ in A:
        for value_ in line_:
            if value_ == -1:
                continue
            else:
                wall_num[value_] += 1
    ans = 0
    for i in range(10):
        ans += wall_num[i] * minimum_distance[i]
    print(ans)


if __name__ == '__main__':
    main()
