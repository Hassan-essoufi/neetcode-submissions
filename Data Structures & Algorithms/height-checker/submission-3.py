class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        p = 0
        for i in range(len(heights)):    
            if heights[i] != expected[i]:
                p += 1
        return p
