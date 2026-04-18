class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums) -1
        result = []
        while left <= right:
            x = nums[left]**2
            y = nums[right]**2
            if x >= y:
                result.append(x)
                left += 1
            else:
                result.append(y)
                right -= 1
        return result[::-1]