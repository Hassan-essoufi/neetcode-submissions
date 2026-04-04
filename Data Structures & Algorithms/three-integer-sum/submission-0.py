class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        l =[]
        i = 0
        nums = sorted(nums)
        while i <len(nums)-1:
            target = nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == -target:
                    h = sorted([nums[j], nums[k], target])
                    if h not in l:
                        l.append(h)
                    j = j+1
                    k = k-1
                elif nums[j] + nums[k] < -target:
                    j = j+1
                else :
                    k = k-1
            i = i+1
        return l