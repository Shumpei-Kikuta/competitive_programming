import numpy as np
import math
import sys

sys.setrecursionlimit(10000000)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    N = int(input())
    S = []
    for i in range(N):
        s = input()
        s = sorted(s)
        S.append(s)
        
    S = sorted(S)
    ans = 0
    num = 0
    for i in range(N):
        if i < N - 1 and S[i] == S[i + 1]:
            num += 1
        else:
            if num == 0:
                continue
            else:
                ans += combinations_count(num + 1, 2)
            num = 0
    print(ans)
                

if __name__ == '__main__':
    main()