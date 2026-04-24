class Solution:
    def arrangeCoins(self, n: int) -> int:
        p = []
        rest = n
        for i in range(1,n):
            if i > rest:
                return len(p)
            p.append(i)
            rest = rest -i
        return len(p) if len(p) > 1 else 1