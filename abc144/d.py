import sys
sys.setrecursionlimit(10000000)
import math

def main():
    a, b, x = map(int, input().split())
    k = x / (a ** 2)
    if 2 * k > b:
        tan = 2 * (k - b) / a
        print(abs(math.degrees(math.atan(tan))))
    else:
        tan = (b ** 2) / (2 * a * k)
        print(abs(math.degrees(math.atan(tan))))


if __name__ == '__main__':
    main()
