class Solution:
    def minOperations(self, s: str) -> int:
        p = 0
        s = list(s)
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                if s[i-1] == '1':
                    s[i] = '0'
                else:
                    s[i] = '1'
                p += 1
        return p