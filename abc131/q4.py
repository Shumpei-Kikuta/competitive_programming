import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def main():
    N = int(input())
    jobs = []
    for i in range(N):
        time_consume, deadline = map(int, input().split())
        jobs.append([deadline, time_consume])
    jobs = sorted(jobs)
    # print(jobs)
    time_ = 0
    for i in range(N):
        time_ += jobs[i][1]
        if (time_ <= jobs[i][0]):
            # 締め切りより時間が立っていなければ、
            pass
        else:
            print("No")
            break
    else:
        print("Yes")



if __name__ == '__main__':
    main()