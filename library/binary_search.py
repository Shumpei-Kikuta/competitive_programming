"""bisectを使ってbanary_searchする"""

import bisect
import math

def main():
    n = int(input())
    S = [int(c) for c in input().split(" ")]
    q = int(input())
    T = [int(c) for c in input().split(" ")]

    num = 0
    for i in range(q):
        x = T[i]
        idx = bisect.bisect_left(S, x)
        # print(idx)
        # print(S[idx])
        if ((idx < n) and (S[idx] == x)):
            num += 1
        else:
            continue

    print(num)
if __name__ == '__main__':
    main()