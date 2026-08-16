from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 1:
            return nums[0]

        @lru_cache(maxsize=None)
        def dp(i, r):
            if i >= r:
                return 0
            return max(dp(i+1, r), dp(i+2, r) + nums[i])

        return max(dp(0, len(nums)-1), dp(1, len(nums)))