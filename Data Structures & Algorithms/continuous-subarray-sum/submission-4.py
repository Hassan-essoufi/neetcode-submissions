class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            total = nums[i]
            for j in range(i+1, len(nums)):
                total += nums[j]
                if (j - i + 1) >= 2 and total % k == 0:
                    return True
        return False
        