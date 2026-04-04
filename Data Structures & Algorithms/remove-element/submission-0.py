from collections import Counter
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = len(list(nums))
        if len(nums) == 0:
            return 0
        count = Counter(nums)
        for i in range(count[val]):
            nums.remove(val)
        return p - count[val]
