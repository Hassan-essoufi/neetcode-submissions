class Solution:

    def largestNumber(self, nums: List[int]) -> str:

        for i  in range(len(nums)):
            for j in range(i+1,len(nums)):
                if str(nums[i]) + str(nums[j]) <= str(nums[j])+ str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        result = "".join(map(str, nums))
        return "0" if result[0] == "0" else result