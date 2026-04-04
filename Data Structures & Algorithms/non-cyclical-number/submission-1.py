class Solution:
    def isHappy(self, n: int) -> bool:
        l = []
        if n == 1:
            return True
        while n > 1 and n not in l:
            l.append(n)
            som = sum(int(i)**2 for i in str(n))
            if som == 1:
                return True
            n = som
        return False 