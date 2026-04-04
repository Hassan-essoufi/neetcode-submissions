class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        min1 = 0
        max1 = len(matrix)-1
        while min1 <= max1:
            n = min1 + (max1- min1)//2 
            if matrix[n][0] <= target and  target <= matrix[n][-1]:
                lower = 0
                higher = len(matrix[n])-1
                while lower <= higher:
                    m = lower + (higher-lower)//2
                    if matrix[n][m] == target:
                        return True
                    elif matrix[n][m] < target:
                        lower = m+1
                    else:
                        higher = m-1
                return False 
            elif matrix[n][0] > target:
                max1 = n-1
            else:
                min1 = n+1

        return False
