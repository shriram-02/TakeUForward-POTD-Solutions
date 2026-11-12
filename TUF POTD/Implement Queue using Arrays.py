class ArrayQueue:
    def __init__(self):
        self.capacity = 100
        self.arr = [0] * self.capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def push(self, x: int) -> None:
        if self.size == self.capacity:
            return
        self.arr[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def isEmpty(self) -> bool:
        return self.size == 0