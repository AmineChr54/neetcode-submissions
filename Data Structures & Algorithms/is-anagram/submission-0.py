class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        maps = {}
        mapt = {}
        for i in range(len(s)):
            maps[s[i]] = maps.get(s[i], 0) + 1
            mapt[t[i]] = mapt.get(t[i], 0) + 1
        for key in maps:
            if not key in mapt or maps[key] != mapt[key]:
                return False
        return True