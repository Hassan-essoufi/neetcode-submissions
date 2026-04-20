class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        p = len(words)
        for x in words:
            for i in range(len(x)):
                if x[i] not in allowed:
                    p -= 1
                    continue
        return p
