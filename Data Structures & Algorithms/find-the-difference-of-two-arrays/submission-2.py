class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        p = []
        k = []
        l = []
        for x in nums1:
            if x not in nums2 and x not in k:
                k.append(x)
        for y in nums2:
            if y not in nums1 and y not in l:
                l.append(y)
        p.append(k)
        p.append(l)
        return p