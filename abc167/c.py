import sys
sys.setrecursionlimit(10000000)
import numpy as np



def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    INF = 10 ** 10
    ans = INF
    for i in range(N):
        lists = [int(c) for c in input().split()]
        ci = lists[0]
        ai = lists[1:]
        C.append(ci)
        A.append(ai)


    for i in range(1 << N):
        ability = np.zeros((M, ))
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                ability += np.array(A[j])
                cost += C[j]
        if sum(ability >= X) == M:
            ans = min(ans, cost)

    if ans == INF:
        print(-1)
    else:
        print(ans)
    

    
    



if __name__ == '__main__':
    main()
