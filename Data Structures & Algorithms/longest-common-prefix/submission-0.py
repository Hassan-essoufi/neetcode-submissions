class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l =""
        m = min(len(ss) for ss in strs)
        for j in range(m):
            for i in range(1,len(strs)):
                if strs[0][j] != strs[i][j]:
                    return l
            l += strs[0][j]
        return l