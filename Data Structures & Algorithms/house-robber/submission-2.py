from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i):
            if i >= len(nums):
                return 0
            return max(dp(i+1), dp(i+2) + nums[i])
        return dp(0)
