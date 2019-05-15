nil = -1

class HashTable():
    def __init__(self):
        self.__m = 1046527
        self.lists = [nil] * self.__m

    def __calc_key(self, x: str):
        # stringのxをint型に変更する.keyは0-self.__mまでの値をとる
        size = len(x)
        sumkey = 0
        p = 1
        for i in range(size):
            key = 0
            if x[i] == "A":
                key = 1
            elif x[i] == "C":
                key = 2
            elif x[i] == "G":
                key = 3
            elif x[i] == "T":
                key = 4
            sumkey += p * key
            p *= 5
        return sumkey

    def __h1(self, intkey):
        # 1個目のhash関数，returnは0-self,__mまでのint
        return intkey % self.__m

    def __h2(self, intkey):
        # 2個目のhash関数， returnは0-self,__mまでのint
        return 1 + intkey % (self.__m - 1)

    def insert(self, x):
        # xを挿入する，まずkeyをint型へ計算し，値から対応するメモリに格納する．その際に衝突を考慮
        intkey = self.__calc_key(x)
        i = 0
        while(True):
            hash_value = (self.__h1(intkey) + i * self.__h2(intkey)) % self.__m
            if (self.lists[hash_value] == nil):
                self.lists[hash_value] = x
                break
            else:
                pass
                i += 1

    def find(self, x):
        # xを探す，まずxをint型へ計算し，対応するメモリを見つける
        intkey = self.__calc_key(x)
        i = 0
        while(True):
            hash_value = (self.__h1(intkey) + i * self.__h2(intkey)) % self.__m
            if (self.lists[hash_value] == x):
                return True
            elif self.lists[hash_value] == nil:
                return False
            else:
                pass 
                i += 1

def main():
    hash = HashTable()
    n = int(input())
    for _ in range(n):
        command, key = input().split()
        # print(command, key)
        if (command[0] == 'i'):
            hash.insert(key)
        else:
            if hash.find(key):
                print("yes")
            else:
                print("no")
        

if __name__ == '__main__':
    main()