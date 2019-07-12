import math

def counting_sort(N, A, k):
    C = [0] * (k + 1)
    B = [0] * (N + 1)
    for element in A:
        C[element] += 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    for i in range(N - 1, -1, -1):
        element = A[i]
        B[C[element] - 1] = element
        C[element] -= 1
        # print(B)
    return B

def main():
    N = int(input())
    A = [int(c) for c in input().split()]
    B = counting_sort(N, A, max(A))
    # print(B)
    for i in range(N):
        print(B[i], end="")
        if i != N-1:
            print(end=" ")
    print()


if __name__ == '__main__':
    main()