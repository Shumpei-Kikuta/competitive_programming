from math import ceil
import numpy as np

N, K = [int(c) for c in input().split()]
A = np.array([int(c) for c in input().split()])

min_num = 10000000
min_idx = np.argmin(A)
for i in range(K):
    # print(min_num)
    if ((min_idx - K + i + 1< 0) | (min_idx + i> N - 1)):
        continue
    else:
        min_num = min(min_num, 1 + ceil((min_idx - K + 1 + i)/(K - 1)) + ceil((N - min_idx - i - 1)/(K - 1)))
print(min_num)
