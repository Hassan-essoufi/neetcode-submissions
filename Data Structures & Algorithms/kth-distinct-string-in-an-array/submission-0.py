from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        t = Counter(arr)
        p = []
        for x in arr:
            if t[x] == 1:
                p.append(x)
        return p[k-1] if k <= len(p) else ""
