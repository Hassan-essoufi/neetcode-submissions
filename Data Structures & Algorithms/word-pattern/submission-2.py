class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p ={}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in p:
                if s[i] not in p.values():
                    p[pattern[i]] = s[i]
                else:
                    return False
            if p[pattern[i]] != s[i]:
                return False
        return True