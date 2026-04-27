class Solution:
    memory = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.memory:
            return self.memory[n]
        else :
            self.memory[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memory[n]