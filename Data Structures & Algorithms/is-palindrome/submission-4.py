class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        p1=0
        p2=len(s)-1
        mid = (len(s) - 1)/2
        def alphanum(c):
            if 'a'<=c<='z' or '0'<=c<='9':
                return True
            return False
        while p1 < p2:
            while not alphanum(s[p1]) and p1 < p2:
                p1 += 1
            while not alphanum(s[p2]) and p1 < p2:
                p2 -= 1
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
