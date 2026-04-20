from collections import Counter
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        p = []
        for x in emails:
            aroba = x.index('@')
            
            
            if '+' in x:
                plus = x.index('+')
                if plus < aroba:
                    x = x[:plus] + x[aroba:]

            h = Counter(x[:aroba])['.']
            for i in range(h):
                   x = x.replace(".", "", 1)
                
            if x not in p :
                p.append(x)
        return len(p)