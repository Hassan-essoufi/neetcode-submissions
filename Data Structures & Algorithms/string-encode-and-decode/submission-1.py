class Solution:

    def encode(self, strs: List[str]) -> str:

        s = strs[0]
        for i in strs[1:]:
            s = s + ' ' + i
        return s
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return [s]
        l = s.split()
        return l