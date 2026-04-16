class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if sum(nums[1:]) == 0:
            return 0
        if sum(nums[:-1]) == 0:
            return len(nums)-1

        for i in range(len(nums)-1):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1