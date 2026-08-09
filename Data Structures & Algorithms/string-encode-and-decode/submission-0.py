class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}:{s}"
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []
        i = 0
        while i < len(s):
            n = ''
            if s[i] <= '9' and s[i] >= '0':
                while s[i] != ':':
                    n += s[i]
                    i += 1
            length = int(n)
            if s[i] == ':':
                result.append(s[i+1:i+length+1])
                i = i + length + 1
        return result
            
