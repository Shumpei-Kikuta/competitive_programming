import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    S = input()
    if S[0] == "S":
        print("Cloudy")
    elif S[0] == "C":
        print("Rainy")
    else:
        print("Sunny")


if __name__ == '__main__':
    main()