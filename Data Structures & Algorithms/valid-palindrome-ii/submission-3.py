
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        
        left = 0
        right = len(s)-1
        while left <= right:
            s_prime = s[:left] + s[left+1:]
            if is_palindrome(s_prime):
                return True
            left += 1
        return False


        
        

            
