class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_pal = s[0]

        def expand_from_center(left: int, right: int) -> str:
            # Expand outwards as long as the boundary characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindromic substring
            return s[left + 1:right]

        for i in range(len(s)):
            # Odd-length palindrome centered at i (e.g. "aba")
            pal1 = expand_from_center(i, i)
            # Even-length palindrome centered between i and i + 1 (e.g. "abba")
            pal2 = expand_from_center(i, i + 1)

            # Update max_pal with the longest found in this iteration
            if len(pal1) > len(max_pal):
                max_pal = pal1
            if len(pal2) > len(max_pal):
                max_pal = pal2

        return max_pal