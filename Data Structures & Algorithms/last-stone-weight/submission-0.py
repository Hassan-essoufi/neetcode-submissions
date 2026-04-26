class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        while len(stones) > 1:

            y = max(stones)  
            stones.remove(y)
            x = max(stones)
            if x == y:
                stones.remove(x)
            else:
                i = stones.index(x)
                stones [i] = y-x
        return stones[0]