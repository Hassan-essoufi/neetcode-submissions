class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                window = nums[i:j+1]
                if sum(window) == k:
                    count += 1 
        return count