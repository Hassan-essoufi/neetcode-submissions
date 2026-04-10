class Solution:
    def reverseBits(self, n: int) -> int:
        
        l = str(n)
        for i in range(31//2):
            l[i], l[31-i] == l[31-i], l[i]
        return int(l)
    
