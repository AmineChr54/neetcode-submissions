class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windows_chars = [0]*26
        l = 0
        max_char = 0
        result = 0

        for r in range(0, len(s)):
            ind_r = ord(s[r]) - ord('A')
            windows_chars[ind_r] += 1
            max_char = max(max_char, windows_chars[ind_r])
            if (r - l + 1) - max_char > k:
                ind_l = ord(s[l]) - ord('A')
                windows_chars[ind_l] -= 1
                l += 1
            else:
                result = max((r - l + 1), result)
        
        return result
            
