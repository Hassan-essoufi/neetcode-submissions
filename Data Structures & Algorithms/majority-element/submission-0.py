from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = Counter(nums)
        for i in nums:
            if t[i] >len(nums)//2:
                return i