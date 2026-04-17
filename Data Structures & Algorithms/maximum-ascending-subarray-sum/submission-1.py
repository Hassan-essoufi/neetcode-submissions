class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        k = 0
        p =[nums[0]]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                p.append(nums[i])
                k = max(k,sum(p))
            else:
                p = [nums[i]]
        return k