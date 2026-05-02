from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        rest = k
        for i in range(len(blocks)-k+1):
            window = blocks[i: i+k]
            rest = min(rest, k-Counter(window)["W"])
        return rest

            