class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        s = []
        right = len(nums)-1
        left = 0
        while left <= right:
            window = nums[left:left+k]
            p = max(window)- min(window)
            if p != 0:
                s.append(p)
            left += 1
        return min(s) if s else 0