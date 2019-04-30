def set_format(name: int):
    """6桁に揃える"""
    formated_name = "{:0=6}".format(name)
    return formated_name

def main():
    N, M = [int(c) for c in input().split()]
    lists = []
    for i in range(M):
        city = i
        prefecture, year = [int(c) for c in input().split()]
        id_ = ""
        lists.append([city, prefecture, year, id_])

    prefectures = [0] * (N + 1)

    #年のソート
    lists.sort(key=lambda x: x[2])

    for i in range(M):
        # 県名
        prefecture_name = lists[i][1]
        lists[i][3] = set_format(prefecture_name) + set_format(prefectures[prefecture_name] + 1)
        prefectures[prefecture_name] += 1

    lists.sort(key=lambda x: x[0])

    for i in range(M):
        print(lists[i][3])

if __name__ =='__main__':
    main()