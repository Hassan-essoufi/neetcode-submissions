class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        m1 = max(nums)
        n1 = min(nums)
        nums.pop(nums.index(m1))
        nums.pop(nums.index(n1))
        m2 = max(nums)
        n2 = min(nums)
        return m1*m2 - n1*n2