class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p = []
        for i in range(len(nums)):
            x = nums[i]**2
            p.append(x)
        return sorted(p)
            