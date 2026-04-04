class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        i = len(nums)-1
        j = 0
        m = 0
        while j <= i:
            if nums[i] < nums[j]:
                m +=1
                j +=1
            else:
                return nums[m]
        return nums[m]
