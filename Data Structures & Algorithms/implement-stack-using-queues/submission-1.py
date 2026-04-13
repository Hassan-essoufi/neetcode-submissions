class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            p = self.queue[-1]
            self.queue.pop()
            return p

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return True if not self.queue else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()