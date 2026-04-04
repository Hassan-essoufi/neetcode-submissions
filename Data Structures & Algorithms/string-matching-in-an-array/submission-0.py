class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = []
        chaque = words[0]
        for s in words:
            for j in words:
                if s!= j and s in j:
                    if s not in l:
                        l.append(s)
        return l
