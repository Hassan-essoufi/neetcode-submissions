class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = nums[0]
        maxx = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                current += nums[i]

            else:
                current = nums[i]
            maxx = max(current,maxx)
        return maxx