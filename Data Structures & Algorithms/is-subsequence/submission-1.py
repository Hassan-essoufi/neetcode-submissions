class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i = 0
        j = 0
        while i < len(s):
            while j < len(t):
                if s[i] == t[j]:
                    i += 1
                j +=1
                if i == len(s):
                    return True
                if j == len(t):
                    return False