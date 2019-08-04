import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def make_successive_count(S: str):
    X = []
    N = len(S)
    num = 1
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            num += 1
        else:
            X.append(num)
            num = 1
    if num != 1:
        X.append(num)
    else:
        X.append(1)
    return X
    

def main():
    S = input()
    N = len(S)
    X = make_successive_count(S)
    assert(len(X) % 2 == 0) #絶対に偶数
    ans = [0] * N

    num = -1
    for i in range(0, len(X), 2):
        left_bound = num + X[i]
        right_bound = num + X[i] + 1
        if ((X[i] + X[i + 1]) % 2) == 0:
            ans[left_bound] = (X[i] + X[i + 1]) // 2
            ans[right_bound] = (X[i] + X[i + 1]) // 2
        else:
            if max(X[i], X[i + 1]) % 2 != 0: #でかいほうが奇数
                #でかいほうが大きくなる
                if X[i] > X[i + 1]:
                    ans[left_bound] = (X[i] + X[i + 1] + 1) // 2
                    ans[right_bound] =  (X[i] + X[i + 1] - 1) // 2
                else:
                    ans[right_bound] = (X[i] + X[i + 1] + 1) // 2
                    ans[left_bound] =  (X[i] + X[i + 1] - 1) // 2
            else:
                #小さいほう大きくなる
                if X[i] > X[i + 1]:
                    ans[right_bound] = (X[i] + X[i + 1] + 1) // 2
                    ans[left_bound] =  (X[i] + X[i + 1] - 1) // 2
                else:
                    ans[left_bound] = (X[i] + X[i + 1] + 1) // 2
                    ans[right_bound] =  (X[i] + X[i + 1] - 1) // 2
                # ans[right_bound] = (X[i] + X[i + 1] + 1) // 2
                # ans[left_bound] =  (X[i] + X[i + 1] - 1) // 2
        num += X[i] + X[i + 1]
    
    n = len(ans)
    for i in range(n):
        print(ans[i], end="")
        if i != n - 1:
            print(end=" ")
    print()
        




if __name__ == '__main__':
    main()