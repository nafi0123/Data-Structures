class MyStack:
    def __init__(self):
        self.arr = []

    def push(self, x) :
        self.arr.append(x)
        return None

    def pop(self) :
        return self.arr.pop()

    def top(self) :
        return self.arr[-1]

    def empty(self) :
        return len(self.arr) == 0
    
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    
print(stack.pop())    
print(stack.empty())  
print(stack.pop())  
print(stack.empty())
