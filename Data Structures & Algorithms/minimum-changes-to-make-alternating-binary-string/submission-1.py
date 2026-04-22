class Solution:
    def minOperations(self, s: str) -> int:
        p = 0
        m = 0
        k = list(s)
        for i in range(1,len(k)):
            if k[i] == k[i-1]:
                if k[i-1] == '1':
                    k[i] = '0'
                else:
                    k[i] = '1'
                p += 1
        h = list(s[::-1])
        for i in range(1,len(h)):
            if h[i] == h[i-1]:
                if h[i-1] == '1':
                    h[i] = '0'
                else:
                    h[i] = '1'
                m += 1

        return min(m,p)