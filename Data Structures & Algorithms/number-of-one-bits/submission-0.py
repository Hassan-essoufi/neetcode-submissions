from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        h = []
        while n >= 1:
            h.append(n%2)
            n = n//2
        counted = Counter(h)
        return counted[1]

        