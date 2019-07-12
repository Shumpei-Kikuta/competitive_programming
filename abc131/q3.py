import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

def main():
    A, B, C, D = [int(c) for c in input().split()]
    N_U = (B) - (A - 1)
    N_C = B // C - (A - 1) // C
    N_D = B // D - (A - 1) // D
    N_C_D = int(B // lcm(C, D) - (A - 1) // lcm(C, D))
    excluded_N_C_D = N_C + N_D - N_C_D
    print(int(N_U - excluded_N_C_D))


if __name__ == '__main__':
    main()