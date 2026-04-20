from collections import Counter
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        p = set()
        for x in emails:
            aroba = x.index('@')
            local, domain = x.split('@')
            if '+' in local:
                plus = local.index('+')
                local = local[:plus]
            local = local.replace('.', '')

            x = local + '@' + domain
            
            p.add(x)
        return len(p)