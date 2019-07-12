import numpy as np
import math

def is_month(month):
    if (month >= 1) and (month <= 12):
        return True
    else:
        return False

def is_yymm(one, two):
    if is_month(two):
        return True
    else:
        return False

def is_mmyy(one, two):
    if is_month(one):
        return True
    else:
        return False
def main():
    S = input()
    one = int(S[0:2])
    two = int(S[2: 4])
    if is_yymm(one, two) and is_mmyy(one, two):
        print("AMBIGUOUS")
    elif(is_yymm(one, two) and ~is_mmyy(one, two)):
        print("YYMM")
    elif(~is_yymm(one, two) and is_mmyy(one, two)):
        print("MMYY")
    else:
        print("NA")

if __name__ == '__main__':
    main()