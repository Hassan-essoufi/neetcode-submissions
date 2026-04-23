class Solution:
    def largestGoodInteger(self, num: str) -> str:
        p = ""
        h = -1
        for i in range(len(num)):
            if list(num[i:i+3]) == [num[i], num[i], num[i]]:
                h = max(int(num[i]), h)
        if h >= 0:
            for i in range(3):
                p = p + str(h)
        return p