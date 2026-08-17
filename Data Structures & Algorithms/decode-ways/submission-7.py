from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        valid = {str(n): chr(n+64) for n in range(1, 27)}
        @lru_cache(maxsize=None)
        def dp(s, i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i ==len(s) -1:
                return 1
            if s[i:i+2] in valid:
                return dp(s, i+2) + dp(s, i+1)
            return dp(s, i+1)
        return dp(s, 0)

        @lru_cache(maxsize=None)
        def dp(s, i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if s[i] == '1':
                if i == len(s) -1:
                    return 1
                else:
                    return dp(s, i+2) + dp(s, i+1)
            if s[i] == '2':
                if i == len(s) -1:
                    return 1
                else:
                    if s[i+1] <= '6':
                        return dp(s, i+2) + dp(s, i+1)
                    else:
                        dp(s, i+1)
            return dp(s, i+1)
        return dp(s, 0)