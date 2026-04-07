class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = [i for i in range(1,num)]
        left = 0
        right = num-1
        while left <= right:
            m = left + (right-left)//2
            if l[m]*l[m] == num:
                return True
            elif l[m]*l[m] > num:
                right -= 1
            else:
                left +=1
        return False