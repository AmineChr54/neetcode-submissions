from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = False
        @lru_cache(maxsize=None)
        def dp(i):
            if i == len(s):   
                return True

            for j in range(i, len(s)):
                if (s[i:j+1] in wordDict) and dp(j+1):
                    nonlocal result
                    result = True
                    return True
        dp(0)
        return result
        
        """result = False
        cur_words = {}
        while
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    cur_words[(j+1,len(s))]
            return False 

        return result"""