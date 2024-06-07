class MyQueue:
    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)
        return None

    def pop(self) -> int:
        return self.arr.pop(0)

    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        return len(self.arr) == 0
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())   
print(queue.pop())    
print(queue.empty())  
print(queue.empty()) 
