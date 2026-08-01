class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > maxp:
                    maxp = prices[j] - prices[i]
        return maxp