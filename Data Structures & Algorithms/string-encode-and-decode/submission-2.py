class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        result = []
        i = 0
        while i < len(s):
            n = ''
            while s[i] != ':':
                n += s[i]
                i += 1
            length = int(n)
            result.append(s[i+1:i+length+1])
            i = i + length + 1
        return result