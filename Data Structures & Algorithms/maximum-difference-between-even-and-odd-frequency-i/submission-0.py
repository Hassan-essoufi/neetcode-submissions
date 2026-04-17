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

        m = max(odd) - min(even)
        n = max(even) - min(odd)
        return n if n>= m else m