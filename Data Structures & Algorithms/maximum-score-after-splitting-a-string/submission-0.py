from collections import Counter
class Solution:
    def maxScore(self, s: str) -> int:
        scores = []
        for i in range(1,len(s)):
            left = Counter(s[:i])
            right = Counter(s[i:])
            scores.append(left['0']+right['1'])
        return max(scores)
            