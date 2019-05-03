import numpy as np
import math

# def compare_each(a, b):
#     """辞書で比べる，もしaの方が小さければ，false，大きければtrue"""
#     if a is None:
#         return True
#     len_a = len(a)
#     len_b = len(b)
#     length = min(len_a, len_b)
#     for i in range(length):
#         if ord(a[i]) < ord(b[i]):
#             return False
#         elif ord(a[i] > b[i]):
#             return True
#     if len_a <= len_b:
#         return False
#     else:
#         return True

# def compare(str_, str_lists, K):
#     """str_listsは昇順で並んでいる．ここにstr_が入るのか戦う"""
#     for i in range(K, 0, -1):
#         print(str_lists[i - 1], str_)
#         if compare_each(str_lists[i - 1], str_):
#            str_lists.insert(i - 1, str_)
#            break
#     return str_lists[:K]


def main():
    s = input()
    K = int(input())
    str_lists = []
    for str_num in range(1, K + 1):
        for i in range(len(s)):
            str_ = s[i: i + str_num]
            if str_ not in str_lists:
                str_lists.append(str_)
    str_lists = sorted(str_lists)
    print(str_lists[K - 1])
    
            

if __name__ == '__main__':
    main()