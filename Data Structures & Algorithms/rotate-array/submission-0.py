class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        k = k % len(nums)
        while k > 0:
            l = nums[len(nums)-1]

            nums.remove(l)
            nums.insert(0,l)
            k = k-1
        return nums
        

