class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+','-','*','/'}
        stack = []
        for token in tokens:
            if token in ops:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == '+':
                    stack.append(num2 + num1)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '/':
                    stack.append(num2 / num1)
                elif token == '*':
                    stack.append(num2 * num1)
            else:
                stack.append(token)
        return int(stack.pop())

                