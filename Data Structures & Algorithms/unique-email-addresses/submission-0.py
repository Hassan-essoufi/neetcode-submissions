from collections import Counter
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        p = []
        for x in emails:
            aroba = x.index('@')
            
            h = Counter(x)['.']
            if '+' in x:
                plus = x.index('+')
                if plus and plus < aroba:
                    x = x[:plus] + x[aroba:]

            for i in range(h-1):
                   x = x.replace(".", "", 1)
                
            if x not in p :
                p.append(x)
        return len(p)