class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        k = nums[0]
        p =[nums[0]]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                p.append(nums[i])

            else:
                p = [nums[i]]
            k = max(k,sum(p))
        return k