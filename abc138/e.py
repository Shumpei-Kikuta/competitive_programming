import numpy as np
import math
import sys
import bisect
sys.setrecursionlimit(10000000)

def main():
    s = input()
    t = input()
    alphabets = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"), None)
    # alphabets = alphabet.copy()
    for key_ in alphabets:
        lists = []
        for i in range(len(s)):
            if key_ == s[i]:
                lists.append(i)
        alphabets[key_] = lists
    now = -1
    count = 0
    for alpha in t:
        if len(alphabets[alpha]) == 0:
            print(-1)
            sys.exit()
        else:
            lists = alphabets[alpha]
            index = bisect.bisect_right(lists, now)
            if index >= len(lists):
                now = -1
                count += len(s)
                now = lists[0]
            else:
                now = lists[index]
            # print(now, count)
    print(count + now + 1)
            







if __name__ == '__main__':
    main()