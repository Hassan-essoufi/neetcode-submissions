class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 0
        pas = 0
        for i in range(len(nums)):
            if i > pas:
                return False
            pas = max(pas, i+ nums[i])
        return True
