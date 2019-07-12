import math

def maxHeapify(heaps, H, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if (left <= H):
        if (heaps[left] > heaps[largest]):
            largest = left
    if (right <= H):
        if (heaps[right] > heaps[largest]):
            largest = right
    if largest == i:
        pass
    else:
        tmp = heaps[i]
        heaps[i] = heaps[largest]
        heaps[largest] = tmp
        heaps = maxHeapify(heaps, H, largest)
    return heaps



def buildMaxHeap(heaps, H):
    for i in range(int(H / 2), 0, -1):
        heaps = maxHeapify(heaps, H, i)
    return heaps

def main():
    H = int(input())
    heaps = [0] #1オリジン
    input_lists = [int(c) for c in input().split()]
    heaps += input_lists
    heaps = buildMaxHeap(heaps, H)
    for i in range(1, H + 1):
        print(" " + str(heaps[i]), end="")
    print()

if __name__ == '__main__':
    main()