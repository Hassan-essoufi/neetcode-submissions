from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i in nums:
            if c[i] % 2 != 0:
                return False
        return True