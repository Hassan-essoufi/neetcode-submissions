class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        for i in range(len(temperatures)-1):
            m = max(temperatures[i+1:])
            if m > temperatures[i]:
                j = temperatures.index(m)-i
            else:
                j = 0
            s.append(j)
        return s