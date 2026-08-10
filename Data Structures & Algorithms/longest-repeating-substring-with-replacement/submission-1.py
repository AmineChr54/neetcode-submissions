class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windows_chars = [0]*26
        l = 0
        long_len_sub = 1
        windows_chars[ord(s[l]) - ord('A')] += 1
        max_char = 1
        result = 1 

        for r in range(1, len(s)):
            ind_r = ord(s[r]) - ord('A')
            windows_chars[ind_r] += 1


            if windows_chars[ind_r] > max_char:
                max_char = max(max_char, windows_chars[ind_r])
                

            if (r - l + 1) - max_char > k:
                ind_l = ord(s[l]) - ord('A')
                windows_chars[ind_l] -= 1
                l += 1
            else:
                result = max((r - l + 1), result)
        
        return result
            
