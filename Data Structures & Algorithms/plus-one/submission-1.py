class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits)-1
        rest = 0
        while i >= 0:
            if digits[i] <= 8:
                digits[i] +=  1
                return digits
            else:
                digits[i] = 0
                rest = 1
                i = i-1
        if rest == 1:
            digits = [rest] + digits
        return digits
