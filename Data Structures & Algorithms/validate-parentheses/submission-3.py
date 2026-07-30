class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in {'[', '(', '{'}:
                stack.append(s[i])
            elif s[i] in {']', ')', '}'}:
                top = stack[-1] if len(stack)!=0 else None
                if top == '(':
                    if s[i] == ')':
                        stack.pop()
                    else:
                        return False
                elif top == '[':
                    if s[i] == ']':
                        stack.pop()
                    else:
                        return False
                elif top == '{':
                    if s[i] == '}':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if len(stack)==0 else False