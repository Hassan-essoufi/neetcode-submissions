from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        p = 0
        for i in range(len(words)):
            k = 0
            for j in range(len(words[i])):
                jj = words[i][j]
                if jj not in chars or Counter(words[i])[jj] > Counter(chars)[jj] :
                    k  += 1
            p += len(words[i]) if k == 0 else 0
        return p
                