class Solution:
    
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a/b) 
            }
        for i in range(len(tokens)):
            if tokens[i] not in ops.keys() :
                stack.append(int(tokens[i]))
            else:
                x = stack.pop()
                y = stack.pop()
                stack.append(ops[tokens[i]](y, x))
        return stack[0]