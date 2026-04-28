class Solution:
    def minOperations(self, s: str) -> int:
        p = 0
        k = list(s)
        for i in range(1,len(k)):
            if k[i] == k[i-1]:
                if k[i-1] == '1':
                    k[i] = '0'
                else:
                    k[i] = '1'
                p += 1
        return p