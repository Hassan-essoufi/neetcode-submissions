class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        p = 0
        j = 0
        for x in words:
            b = True
            for i in x:
                if i not in allowed:
                    b = False
                    break
            if b == True:
                p += 1
            
        return p
