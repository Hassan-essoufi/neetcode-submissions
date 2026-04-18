class Solution:
    def check(self, nums: List[int]) -> bool:
        p = sorted(nums)
        i = 0
        while i <= len(nums)-1:
            t = 0
            for j in range(len(nums)):
                if p[j] != nums[(i+j)%len(nums)]:
                    break
                else :
                    t += 1
            
            if t == len(p):
                return True
            i +=1


        return False
