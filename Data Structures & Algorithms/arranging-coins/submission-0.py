class Solution:
    def arrangeCoins(self, n: int) -> int:
        p = []
        rest = n-1
        for i in range(1,n):
            if i > rest:
                return len(p)
            p.append(i)
            rest = rest -i
