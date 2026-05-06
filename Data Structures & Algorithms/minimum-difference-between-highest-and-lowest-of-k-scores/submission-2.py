class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        min_score = nums[-1] - nums[0]
        for i in range(k,len(nums)):
            min_score = min(min_score, nums[i]-nums[i-k+1])
            
        return min_score




