class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p = []
        for x in nums1:
            if x in nums2 and x not in p:
                p.append(x)

        for y in  nums2:
            if y in nums1 and y not in p:
                p.append(y)
        return p