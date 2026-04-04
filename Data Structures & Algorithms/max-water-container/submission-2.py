class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights[0], heights[1])
        d = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                m  = min(heights[j], heights[i])
                d = max(d, (j-i)*m)

        return d