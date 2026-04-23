from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        counts1 = Counter(ransomNote)
        counts2 = Counter(magazine)

        for i in counts1:
            if i not in counts2:
                return False
            elif counts1[i] > counts2[i]:
                return False
        return True