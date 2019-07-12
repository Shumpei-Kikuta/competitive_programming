import numpy as np
import math

def main():
    N, K = map(int, input().split())
    prob = 0
    for i in range(1, N + 1):
        score = i
        if (score >= K):
            left = N - score + 1
            prob += left / N
            break
        else:
            num = 1
            while(True):
                if (score * 2 < K):
                    num += 1
                    score *= 2
                else:
                    prob += 1/(N * (2)**num)
                    break
    print(prob)


if __name__ == '__main__':
    main()