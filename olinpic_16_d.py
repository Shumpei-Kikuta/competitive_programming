import sys
sys.setrecursionlimit(10000000)

INF = 1000000

def main():
    n, m = map(int, input().split())
    lists = [int(input()) - 1 for i in range(n)]


    dp = [INF for i in range(2 ** m)]

    sum_ = [[0 for j in range(n)] for i in range(m)]

    num_dicts = {}
    for i in range(n):
        if num_dicts.get(lists[i]) is None:
            num_dicts[lists[i]] = 1
        else:
            num_dicts[lists[i]] += 1


    def prepare_sum(n, m, sum_, lists):
        for i in range(m):
            for j in range(n):
                if lists[j] == i:
                    sum_[i][j] = sum_[i][j - 1] + 1 if j != 0 else 1
                else:
                    sum_[i][j] = sum_[i][j - 1] if j != 0 else 0
        return sum_


    def solve(left, S):
        if (1 << m) - 1 == S:
            # すべて並び終えた
            dp[S] = 0
            return 0
        else:
            res = INF
            for i in range(m):
                if (S >> i) & 1:
                    continue
                right = left + num_dicts[i]
                if left == 0:
                    res = min(res, solve(right, S | 1 << i) + num_dicts[i] - sum_[i][right - 1])
                else:
                    res = min(res, solve(right, S | 1 << i) + num_dicts[i] - (sum_[i][right - 1] - sum_[i][left - 1]))
            dp[S] = res
            return res

    sum_ = prepare_sum(n, m, sum_, lists)
    print(solve(0, 0))


if __name__ == '__main__':
    main()