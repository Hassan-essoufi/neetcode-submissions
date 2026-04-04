from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = []
        counts = Counter(nums)
        for x in nums:
            if counts[x] > len(nums)//3 and x not in l:
                l.append(x)
        return l