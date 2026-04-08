class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = []
        p  = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                l.append(p)
                p = 0
            else:
                p +=1
        l.append(p)
        return max(l)
