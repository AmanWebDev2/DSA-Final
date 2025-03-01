class Stack:
    def __init__(self):
        self.arr = []

    def push(self,val:int):
        self.arr.append(val)

    def is_empty(self):
        return len(self.arr) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self.arr.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.arr[-1]

    def size(self):
        return len(self.arr)

    def __str__(self):
        return f"Stack({self.arr})"


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.pop()
print(stack)
print(stack.top())
print(stack.size())