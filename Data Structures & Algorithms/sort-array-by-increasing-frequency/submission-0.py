from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
       p = Counter(nums)
       
       return sorted(nums, key=lambda x: (p[x], -x))
            


        
        