class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if len(order) == 1:
            return s
        s = list(s)
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] not in order:
                    continue
                elif s[i] in order and s[j] in order:
                    x = order.index(s[i])
                    y = order.index(s[j])
                    if x > y:
                        s[i], s[j] = s[j], s[i]
        return ''.join(s)