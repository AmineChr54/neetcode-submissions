class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indices of days still waiting for a warmer day

        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)

        return result