from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
        
        
        min_count = float('inf')
        @lru_cache(maxsize=None)
        def dp(n,count,i):
            if n == amount:
                return count
            if i<0 or n>amount:
                return float('inf')
            return min(dp(n+coins[i], count + 1,i), dp(n, count ,i-1))
        m = dp(0,0,len(coins)-1)
        if m == float('inf'):
            return -1
        else:
            return m
        
        def dp(n, count, i):
            if i<0:
                return
            if n == amount:
                min_count = min(min_count, count)
            dp(n, count, i-1)
            while n + coins[i] < amount:
                n += coins[i]
                count += 1
            dp(n, count, i-1)
        dp(0,0,len(coins) -1)
        return min_count
        
        
        result = 0
        n=0
        i = len(coins) -1

        while n < amount:
            while i >= 0 and n+coins[i] > amount:
                    i -= 1
            n += coins[i]
            result += 1

        if n == amount:
            return result
        else:
            return -1