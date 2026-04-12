class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p = ""
        for i in range(len(t)):
            if t[i] not in s:
                p = p +t[i:]
                return len(p)
        return 0