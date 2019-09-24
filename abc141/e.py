import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

 
def is_match(string, pattern):
    if pattern in string:
        return True
    else:
        return False


def main():
    N = int(input())
    S = input()

    dp = [0] * N

    for i in range(1, N):
        length = dp[i - 1] + 1
        match_string = S[i - length + 1: i + 1]
        matched_string = S[:i+1-length]
        if is_match(matched_string, match_string):
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    
    print(dp[-1])



if __name__ == '__main__':
    main()