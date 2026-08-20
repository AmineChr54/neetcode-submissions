from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        max_len = max((len(word) for word in wordDict), default = 0)

        @lru_cache(maxsize=None)
        def dp(i):
            if i == len(s):   
                return True
            for j in range(i, min(i + max_len, len(s))):
                if (s[i:j+1] in wordDict) and dp(j+1):
                    return True
            return False
        
        return dp(0)

        """
        Time Complexity = O(N*min(N,max_len)*max_len    +   2D)
        Space Complexity = O(N + D)
        """
