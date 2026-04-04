from collections import Counter
class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            h = []
            while i >=1:
                h.append(i%2)
                i = i//2
            l.append(Counter(h)[1])
        return l