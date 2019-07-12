import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    S = input()
    for i in range(3):
        if S[i] == S[i + 1]:
            print("Bad")
            break
    else:
        print("Good")

if __name__ == '__main__':
    main()