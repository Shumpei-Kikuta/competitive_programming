import math

def counting_sort(A, B, k, n):
    C = [0] * (k + 1)

    for i in range(n):
        C[A[i]] += 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for j in range(n - 1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1
    return B


def main():
    n = int(input())
    A = [int(c) for c in input().split()]
    B = [None] * (n + 1)
    k = max(A)
    B = counting_sort(A, B, k, n)[1: ]
    for i in range(len(B)):
        print(B[i], end="")
        if i != len(B) - 1:
            print(end=" ")
    print()

if __name__ == '__main__':
    main()