class Solution:
    def rest(self, target):
        p = target
        while target > 9:
            p = target % 10
            target = target // 10
            
        return p


    def largestNumber(self, nums: List[int]) -> str:

        for i  in range(len(nums)):
            for j in range(i+1,len(nums)):
                if self.rest(nums[i]) <= self.rest(nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        result = "".join(map(str, nums))
        return "0" if result[0] == "0" else result