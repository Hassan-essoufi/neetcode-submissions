class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        end = 0
        left = 0
        right =x
        while left <= right:
            m = left + (right-left)//2
            if m*m == x:
                return m
            elif m*m < x:
                left = m+1
                end =m
            else: 
                right=m-1
        return end