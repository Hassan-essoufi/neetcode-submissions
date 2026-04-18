class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        p = []
        for x in nums1:
            next = -1
            for i in range(len(nums2)-1,-1,-1):
                if nums2[i] > x:
                    next = nums2[i]
                elif nums2[i] == x:
                    break
            p.append(next)

        return p