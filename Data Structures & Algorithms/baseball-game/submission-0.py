class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for x in operations:
            if x == '+':
                s = stack[-1] + stack[-2]
                stack.append(s)
            elif x == 'C':
                stack.pop()
            elif x == 'D' :
                stack.append(2*stack[-1])
            else:
                stack.append(int(x))

        return sum(stack)