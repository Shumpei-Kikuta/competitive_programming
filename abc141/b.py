import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    S = input()
    length = len(S)
    for i in range(length):
        if i % 2 == 0:
            # 奇数番目
            if S[i] not in ["R", "U", "D"]:
                print("No")
                sys.exit()
        else:
            if S[i] not in ["L", "U", "D"]:
                print("No")
                sys.exit()
    print("Yes")


if __name__ == '__main__':
    main()