class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return  False
        d = {')':'(', ']':'[', '}':'{'}
        rest = []
        for bracket in s:
            if bracket in d.values():
                rest.append(bracket)
            elif d[bracket] not in rest or d[bracket] !=rest[-1]:
                return False 
                    
            else:
                rest.pop(-1)
                
                
        return True if len(rest) == 0 else False

