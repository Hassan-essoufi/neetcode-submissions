class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        min_score = nums[-1] - nums[0]
        for i in range(len(nums)-k+1):
            min_score = min(min_score, nums[i+k-1]-nums[i])

        return min_score




