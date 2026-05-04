from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total  = ""
        for x in words:
            total += x
        p = Counter(total)
        for y in p:
            if p[y] % len(words) != 0 :
                return False
        return True

        