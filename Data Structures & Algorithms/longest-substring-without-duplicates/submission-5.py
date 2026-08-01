class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l, maxl = 0, 0
        chars = set()
        chars.add(s[l])
        for r in range(1, len(s)):
            if s[r] in chars:
                maxl = max(maxl, len(s[l:r]))
                while s[l] != s[r]:
                    chars.remove(s[l])
                    l += 1
                l+=1
            else:
                chars.add(s[r])
        r += 1
        maxl = max(maxl, len(s[l:r]))
        return maxl

        """
        for r in range(1, len(s)):
            if s[r] in chars:
                maxl = max(maxl, len(s[l:r]))
                l = r
                chars=set()
                chars.add(s[r])
            else:
                chars.add(s[r])
        r += 1
        maxl = max(maxl, len(s[l:r]))
        return maxl"""