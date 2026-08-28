class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1 or len(s) % 2 == 1:
            return False

        CLOSERS_OPENERS = {
            ")": "(", 
            "}": "{", 
            "]": "["
            }

        stack = []
        for c in s:
            if c in CLOSERS_OPENERS.values():
                stack.append(c)
            elif c in CLOSERS_OPENERS.keys():
                if not stack or stack.pop() != CLOSERS_OPENERS[c]:
                    return False

        return not stack