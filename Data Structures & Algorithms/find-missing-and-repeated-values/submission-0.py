class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = 0
        d = 0
        n = len(grid)
        for val in range(1, n**2+1):
            c = 0
            for i  in range(n):
                for j in range(n):
                    if grid[i][j] == val:
                        c +=1
            if c == 0:
                m = val
            if c == 2:
                d = val
        return [d, m]

