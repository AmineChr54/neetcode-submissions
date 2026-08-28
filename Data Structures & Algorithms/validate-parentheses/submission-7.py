class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1 or len(s) % 2 == 1:
            return False

        CLOSERS_OPENERS = {
            ")": "(", 
            "}": "{", 
            "]": "["
            }
        OPENERS = {"(", "{", "["}
        CLOSERS = {")", "}", "]"}

        stack = []
        for c in s:
            if c in OPENERS:
                stack.append(c)
            elif c in CLOSERS:
                if len(stack) == 0 or stack[-1] != CLOSERS_OPENERS[c]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
