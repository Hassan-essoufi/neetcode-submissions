class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            for j in range(i+1, len(haystack)):
                if haystack[i:j] == needle:
                    return i
        return -1
