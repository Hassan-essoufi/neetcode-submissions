class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        x = 30000
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i]+prices[j] <= money:
                    x = min((prices[i]+prices[j],x))
        
        if x <= money:
            return money-x
        else:
            return money
            