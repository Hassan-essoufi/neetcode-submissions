from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        
        odd = []
        even = []
        for i in counts.values():
            if i%2 == 0:
                even.append(i)

            else:
                odd.append(i)

        return max(odd) - min(even)
    