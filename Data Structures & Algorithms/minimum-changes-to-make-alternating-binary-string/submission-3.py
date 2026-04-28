class Solution:
    def minOperations(self, s: str) -> int:
        p = [0,0]
        k = [list(s), list(s[::-1])]
        for j in range(2):
            h = k[j]
            for i in range(1,len(h)):
                if h[i] == h[i-1]:
                    if h[i-1] == '1':
                        h[i] = '0'
                    else:
                        h[i] = '1'
                    p[j] += 1
        return min(p)
