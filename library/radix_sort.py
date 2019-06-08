import math
from typing import List

def counting_sort(N, A, idx):
    C = [0] * 10
    B = [0] * (N)
    for element in A:
        element = int(element[idx])
        C[element] += 1
    for i in range(1, 10):
        C[i] = C[i] + C[i - 1]
    for i in range(N - 1, -1, -1):
        element = A[i]
        int_element = int(A[i][idx])
        B[C[int_element] - 1] = element
        C[int_element] -= 1
    # print(B)
    return B

def preprocess(A, N, d) -> List[str]:
    """全ての桁数をdに揃える
    """
    for i in range(N):
        A[i] = str(A[i])
        if len(str(A[i])) < d:
            add_zero = d - len(str(A[i]))
            A[i] = "0" * add_zero + A[i]
    return A


def main():
    N = int(input())
    A = [int(c) for c in input().split()]
    k = max(A)
    d = len(str(k))
    A = preprocess(A, N, d)
    B = A
    for i in range(d - 1, -1, -1):
        B = counting_sort(N, B, i)
    for i in range(N):
        print(int(B[i]), end="")
        if i != N-1:
            print(end=" ")
    print()


if __name__ == '__main__':
    main()