from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = []
        l = Counter(nums).most_common(k)
        for i in range(len(l)):
            r.append(l[i][0])
        return r
     
