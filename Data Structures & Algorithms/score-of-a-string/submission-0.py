class Solution:
    def scoreOfString(self, s: str) -> int:
        p = 0
        for i in range(1, len(s)):
            p += abs(ord(s[i]) - ord(s[i-1]))
        return p