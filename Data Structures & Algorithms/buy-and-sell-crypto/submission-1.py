class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, maxp = 0, 0
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
        return maxp

        """maxp = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > maxp:
                    maxp = prices[j] - prices[i]
        return maxp"""