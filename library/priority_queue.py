import math
import sys

INF = 1000000

class PriorityQueue():
    def __init__(self):
        self.__H = 0
        self.__heaps = [0] * INF # 1オリジン

    def insert(self, x):
        """xを挿入する
        要素数を増やして，そこにとりあえず格納
        親と比較していき，いけるとこまで上へ
        """
        self.__H += 1
        self.__heaps[self.__H] = x
        now = self.__H
        while(True):
            if int(now / 2) >= 1:
                parent = int(now / 2)
                if (self.__heaps[now] > self.__heaps[parent]):
                    tmp = self.__heaps[now]
                    self.__heaps[now] = self.__heaps[parent]
                    self.__heaps[parent] = tmp
                    now = parent
                else:
                    break
            else:
                break

        # print(self.__heaps[1:self.__H + 1])

    def __maxHeapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        largest = i
        if (left <= self.__H):
            if (self.__heaps[left] > self.__heaps[largest]):
                largest = left
        if (right <= self.__H):
            if (self.__heaps[right] > self.__heaps[largest]):
                largest = right
        if largest == i:
            pass
        else:
            tmp = self.__heaps[i]
            self.__heaps[i] = self.__heaps[largest]
            self.__heaps[largest] = tmp
            self.__maxHeapify(largest)
                
    
    def extract(self):
        """
        一番上を取る
        一番下のやつを一番上に移動し，maxheapifyを行う
        """
        value = self.__heaps[1]
        self.__heaps[1] = self.__heaps[self.__H]
        self.__H -= 1
        self.__maxHeapify(1)
        # print(self.__h/eaps)
        print(self.__heaps[1:self.__H + 1])
        return value

def main():
    pqueue = PriorityQueue()
    while (True):
        command = input()
        if (command == "end"):
            sys.exit()
        elif (command[0] == "e"):
            # extract
            value = pqueue.extract()
            print(value)
        else:
            # insert
            value = int(command.split()[1])
            pqueue.insert(value)

        

if __name__ == '__main__':
    main()