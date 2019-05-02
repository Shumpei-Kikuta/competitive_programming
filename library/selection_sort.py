"""通常はsorted(list, reverse=True)を使う"""
"""
    挿入ソート: トランプの並び替え．ある程度整列されていれば，O(N)でいける，降順を昇順にするときO(N^2)
    バブルソート: 常に0(N^2)
    選択ソート: 最小値を探すを繰り返す，常にO(N^2)．不安定
"""

def selection_sort(lists: list) -> list:
    N = len(lists)
    for i in range(1, N):
        j = i - 1
        tmp = lists[i]
        while((tmp <= lists[j]) and (j >= 0)):
            lists[j + 1] = lists[j]
            j -= 1
        lists[j + 1] = tmp
    return lists


if __name__ == '__main__':
    # 単純な例
    test1 = [1, 4, 7, 10, 5, 2, 6]
    assert(selection_sort(test1) == [1, 2, 4, 5, 6, 7, 10])
    # 降順な例
    test2 = [10, 8, 6, 4, 2, 0]
    assert(selection_sort(test2) == [0, 2, 4, 6, 8, 10])
    # 並び替えない
    test3 = [0,1, 2, 3, 4]
    assert(selection_sort(test3) == [0,1, 2,3 , 4])
    #極端な例
    test4 = [1]
    assert(selection_sort(test4) == test4)