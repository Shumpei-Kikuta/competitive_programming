import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    S = int(input())
    # if S <= 10e9:
    #     X1 = 0
    #     Y1 = 0
    #     X2 = S
    #     Y2 = 0
    #     X3 = 0
    #     Y3 = 1
    # else:

    root_S = np.sqrt(S)
    l = int(np.ceil(root_S))
    X3Y2 = l ** 2 - S
    X1 = 0
    Y1 = 0
    X2 = l
    Y3 = l
    Y2 = l**2 - S
    X3 = 1
    print(X1, Y1, X2, Y2, X3, Y3)




if __name__ == '__main__':
    main()