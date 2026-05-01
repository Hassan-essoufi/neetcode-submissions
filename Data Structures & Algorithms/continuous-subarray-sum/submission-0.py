class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if len(nums[i:j]) >= 2 and  sum(nums[i:j]) % k == 0:
                    return True

        return False