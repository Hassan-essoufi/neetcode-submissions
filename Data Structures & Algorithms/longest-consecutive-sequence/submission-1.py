class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        max_streak = 0
        
        for num in nums_set:
   
            if num - 1 not in nums_set:
                current = num
                streak = 1
                
                while current + 1 in nums_set:
                    current += 1
                    streak += 1
                
                max_streak = max(max_streak, streak)
        
        return max_streak
