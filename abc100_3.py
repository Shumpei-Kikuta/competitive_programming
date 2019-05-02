from math import ceil

N = int(input())
A = [int(c) - i for i, c in enumerate(input().split())]

A.sort()

median = A[ceil((N - 1) /2)]

num = 0
for i in range(N):
    num += abs(A[i] - median)

print(num)