class Stack():
    def __init__(self):
        self.top = 1
        self.lists = []
    
    def is_empty(self):
        if (self.top <= 1):
            return True
        else:
            return False
    
    def push(self, x):
        self.lists.append(x)
        self.top += 1
    
    def pop(self):
        if self.top > 1:
            self.top -= 1
        else:
            print("there aren't enough values in Stack")


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert(stack.top == 2)