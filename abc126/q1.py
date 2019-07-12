import numpy as np
import math

def main():
    n, k = map(int, input().split())
    string = input()
    new_string = ""
    for i in range(len(string)):
        if i == k - 1:
            new_string += string[i].lower()
        else:
            new_string += string[i]
    print(new_string)

if __name__ == '__main__':
    main()