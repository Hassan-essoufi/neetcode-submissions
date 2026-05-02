class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        if len(self.stack) == 1:
            return 1
        p = 0
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] <= price:
                p += 1
            if self.stack[i] > price:
                return p

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)