class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while high >= low:
            m = low + (high - low) // 2 
            if nums[m] == target:
                return m
            elif nums[m] < target:
                low = m+1     
            else:

                high = m-1
        return -1