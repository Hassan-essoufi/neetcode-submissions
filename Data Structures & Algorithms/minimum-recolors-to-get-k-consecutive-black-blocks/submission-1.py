from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_op = k
        for i in range(len(blocks)-k+1):
            window = blocks[i: i+k]
            count =  Counter(window)
            min_op = min(min_op,count['W'])
        
        return min_op