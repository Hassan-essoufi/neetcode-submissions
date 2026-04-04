from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counted = Counter(nums)
        for i in nums:
            if counted[i] == 1:
                return i