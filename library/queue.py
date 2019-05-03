LEN = 100000

class Queue():
    def __init__(self):
        self.left = 0
        self.right = 0
        self.lists = [None] * LEN
        self.front = self.lists[self.left]
        self.size = self.right - self.left

    def push(self, x):
        self.lists[self.right] = x
        self.right += 1
        self.right %= LEN
        self.front = self.lists[self.left]
        self.size = self.right - self.left
    
    def pop(self):
        self.left += 1
        self.left %= LEN
        self.front = self.lists[self.left]
        self.size = self.right - self.left


if __name__ == '__main__':
    queue = Queue()
    queue.push(2)
    queue.push(5)
    assert(queue.front == 2)
    queue.pop()
    queue.push(11)
    queue.push(14)
    assert(queue.front == 5)
    assert(queue.size == 3)


    
