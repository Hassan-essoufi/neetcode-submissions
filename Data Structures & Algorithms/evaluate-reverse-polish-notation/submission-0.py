class Solution:
    
    stack = []
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
            }
        for i in range(len(tokens)):
            if tokens[i] not in ops.keys() :
                self.stack.append(int(tokens[i]))
            else:
                x = self.stack.pop()
                y = self.stack.pop()
                self.stack.append(ops[tokens[i]](x, y))
        return self.stack[0]