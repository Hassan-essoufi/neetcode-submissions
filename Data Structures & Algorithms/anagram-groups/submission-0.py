from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        h = []
        l = set()
        for x in strs:
            if x not in l:
                group = []
                for y in strs:
                    if Counter(x) == Counter(y):
                        group.append(y)
                        l.add(y)
                h.append(group)
        return h