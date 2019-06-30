import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    S = input()
    num_dicts = {}
    for i in range(len(S)):
        if S[i] not in num_dicts:
            num_dicts[S[i]] = 1
        else:
            num_dicts[S[i]] += 1
    for key_, value_ in num_dicts.items():
        if value_ == 2:
            pass
        else:
            print("No")
            sys.exit()
    else:
        if len(num_dicts) == 2:
            print("Yes")
            sys.exit()
        else:
            print("No")
            sys.exit()


if __name__ == '__main__':
    main()