class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n1 = len(s1)
        map1 = {}
        for c in s1:
            map1[c] = map1.get(c, 0) + 1

    
        map2 = {}
        for i in range(n1):
            map2[s2[i]] = map2.get(s2[i], 0) + 1
        if map1 == map2:
            return True

        for i in range(n1, len(s2)):
            if map2[s2[i-n1]] == 1:
                map2.pop(s2[i-n1])
            else:
                map2[s2[i-n1]] -= 1
            map2[s2[i]] = map2.get(s2[i], 0) + 1
            if map1 == map2:
                return True
        return False