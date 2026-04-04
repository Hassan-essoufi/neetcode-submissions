class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(len(nums)//2):
            nums[i] , nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
        for i in range(k//2):
            nums[i] , nums[k-1-i] = nums[k-1-i], nums[i]
        
        for i in range((len(nums)-k)//2):
            nums[i+k] , nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i+k]
        
        return nums
        

