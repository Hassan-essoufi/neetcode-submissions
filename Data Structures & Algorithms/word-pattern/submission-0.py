class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p ={}
        s = s.split()
        for i in range(len(pattern)):
            if pattern[i] not in p:
                p[pattern[i]] = s[i]
            if p[pattern[i]] != s[i]:
                return False
        return True