class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else :
                return -1
        j = 0
        i = len(nums)-1
        while j <= i:
            m = j + (i-j)//2
            if nums[m] == target:
                return m
            elif nums[j] <= nums[m] :
                if nums[j] <= target and target < nums[m]:
                    i = m-1
                else:
                    j = m+1
            else:
                if nums[i] >= target and target > nums[m]:
                    j = m+1
                else:
                    i = m-1
   
        return -1