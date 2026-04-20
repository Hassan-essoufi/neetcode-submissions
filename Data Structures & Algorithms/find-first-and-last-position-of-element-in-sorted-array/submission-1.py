class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target not in nums:
            return [-1, -1]

        left = 0
        right = len(nums)-1
        p = []
        while left <= right:
            m = (right+left)//2 
            if nums[m] == target:
                p.append(m)
                if m+1 < len(nums) and nums[m+1] == target:
                    p.append(m+1)
                elif m-1 >-1 and nums[m-1] == target:
                    p.append(m-1)
                else:
                    p.append(m)
                return sorted(p)
            elif nums[left] < target:
                left = m+1
            else:
                right = m-1