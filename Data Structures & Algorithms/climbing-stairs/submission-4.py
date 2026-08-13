from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(n):
            if n<=2:
                return n
            return dp(n-1) + dp(n-2) 
        
        return dp(n)
                