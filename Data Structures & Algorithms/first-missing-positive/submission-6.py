class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if min(nums) > 1 or max(nums) < 1:
            return 1
        for i in range(min(nums), max(nums)+2, 1):
            if i not in nums and i > 0: 
                return i