class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        l = ""
        m = min(len(word1), len(word2))
        while i < m and j < m:
            l += word1[i] + word2[j]
            i = i+1
            j = j+1
        if len((word1))> len(word2):
            l = l +word1[m:]
        else:
            l = l + word2[m:]
        return l
     
