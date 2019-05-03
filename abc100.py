N = int(input())

num = 0
A =[int(i) for i in input().split()]

for i in range(N):
    while(A[i] % 2 == 0):
        num += 1
        A[i] /= 2

print(num)
