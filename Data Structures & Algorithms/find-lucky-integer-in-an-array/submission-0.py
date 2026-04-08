from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        p =[]
        for i in counts:
            if i == counts[i]:
                p.append(i)
        return max(p) if p else -1
        