class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for data in details:
            if int(data[11:13]) > 60:
                c += 1
        return c