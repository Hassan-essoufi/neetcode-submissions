class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        right = len(nums)-1
        while low <= right:
            m = low + (right-low)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                low = m+1
            else:
                right = m-1
        return low
            