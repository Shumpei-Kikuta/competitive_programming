import sys
sys.setrecursionlimit(10000000)
 

def main():
    N = int(input())
    A = [int(c) for c in input().split()]


    dicts = {i: 0 for i in range(1, N + 1)}

    for i in A:
        dicts[i] += 1

    for _, v in dicts.items():
        print(v)



if __name__ == '__main__':
    main()
