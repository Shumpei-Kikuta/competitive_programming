"""
pythonでstackとqueueはどちらもdeque(double ended-queue)で実装可能
stack
stack = deque()
stack.push(1)
stack.pop()

queue = deque()
queue.push(12)
queue.popleft()
"""


from collections import deque

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
        self.front = self.__get_front()
        self.size = self.right - self.left
    
    def pop(self):
        self.left += 1
        self.left %= LEN
        self.front = self.__get_front()
        self.size = self.right - self.left if self.right >= self.left else self.right + LEN - self.left

    def __get_front(self):
        return self.lists[self.left]


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

    queue = deque()
    queue.append(2)
    queue.append(5)
    assert(len(queue) == 2)
    queue.popleft()
    assert(len(queue) == 1)
    assert(queue[len(queue)-1] == 5)





    
