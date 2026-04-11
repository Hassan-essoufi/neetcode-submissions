class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        right = len(nums)-1
        left = 0
        while left < right:
            if nums[right] == 0:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1
        