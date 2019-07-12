import numpy as np
import math

# class Place():
#     def __init__(self, idx, x, cost):
#         self.idx = idx
#         self.x = x
#         self.cost = cost

# def calc_distance(max_value, min_value):
#     if (max_value < 0):
#         return 2 * abs(max_value) + 2 * abs(max_value - min_value)
#     elif (min_value > 0):
#         return 2 * abs(min_value) + 2 * abs(max_value - min_value)
#     else:
#         return 2 * (abs(min_value) + abs(max_value))


# def calc_cost(X):
#     N = len(X)
#     assert(calc_distance(3, -1) == 8)
#     assert(calc_distance(-1, -3) == 6)
#     assert(calc_distance(5, 3) == 10)
#     for i in range(N):
#         if i == 0:
#             X[i].cost = calc_distance(X[N - 1].x, X[1].x)
#         elif i == N - 1:
#             X[i].cost = calc_distance(X[N - 2].x, X[0].x)
#         else:
#             X[i].cost = calc_distance(X[N - 1].x, X[0].x)
#     return X


def main():
    N = int(input())

    X = [int(c) for c in input().split()]
    X.insert(0, 0)
    X.append(0)
    Y = []
    length = len(X)
    for i in range(length - 1):
        Y.append(X[i + 1] - X[i])
    normal_distance = 0
    for i in range(length - 1):
        normal_distance += abs(Y[i])
    for i in range(N):
        if Y[i + 1] * Y[i] >= 0: 
            print(normal_distance)
        else:
            print(normal_distance - 2 * min(abs(Y[i]), abs(Y[i + 1])))

    # input_lists = [int(c) for c in input().split()]
    # for i in range(N):
    #     x = input_lists[i]
    #     place = Place(i, x, None)
    #     X.append(place)

    # X = sorted(X, key=lambda t: t.x)

    # assert(X[0].x == min(input_lists))

    # X = calc_cost(X)

    # X = sorted(X, key=lambda X: X.idx)

    # for i in range(N):
    #     print(X[i].cost)

if __name__ == '__main__':
    main()