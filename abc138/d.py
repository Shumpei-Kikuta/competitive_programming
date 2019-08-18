import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N, Q = map(int, input().split())
    edges = {}
    for i in range(N-1):
        a, b = map(int, input().split())
        edges[b] = a # 子: 親

    questions = {}
    for i in range(Q):
        p, x = map(int, input().split())
        if questions.get(p) is None: 
            questions[p] = x
        else:
            questions[p] += x

    qustions = sorted(questions.items(), key=lambda x:x[0])

    points = [0] * (N + 1)
    if questions.get(1) is None:
        points[1] = 0
    else:
        points[1] = questions[1]

    for i in range(2, N+1):
        if questions.get(i) is None:
            points[i] = points[edges[i]]
        else:
            points[i] = points[edges[i]] + questions[i]

    for i in range(1, N+1):
        print(points[i], end="")
        if i != N:
            print(end=" ")
    print("")



if __name__ == '__main__':
    main()