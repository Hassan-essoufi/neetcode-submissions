import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)-1):
            right = nums[:i]
            left = nums[i+1:]
            l.append(int(math.prod(right)*math.prod(left)))
        l.append(int(math.prod(nums[:len(nums)-1])))
        return l
            