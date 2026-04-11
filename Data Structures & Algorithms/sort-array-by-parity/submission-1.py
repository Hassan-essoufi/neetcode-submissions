class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] % 2 == 0: 
                left += 1
            else:
                nums.append(nums[left])
                nums.pop(left)

                right -= 1
        return nums