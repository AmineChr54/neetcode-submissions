from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        max_len = max((len(word) for word in wordDict))

        
        @lru_cache(maxsize=None)
        def dp(i):
            if i == len(s):   
                return True
            for j in range(i, i+max_len):
                if (s[i:j+1] in wordDict) and dp(j+1):
                    return True
            return False
        
        return dp(0)
