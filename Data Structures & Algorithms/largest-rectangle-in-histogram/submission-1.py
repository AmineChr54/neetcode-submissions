class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(len(heights)):
            if stack:
                if heights[i] < heights[stack[-1]]: #VIOLATION
                    while stack and heights[i] < heights[stack[-1]]:
                        cur = stack.pop()
                        right = i-1
                        left = stack[-1]+1 if stack else 0
                        max_area = max(max_area, (right-left+1)*heights[cur])
                    stack.append(i)
                #elif heights[i] > heights[stack[-1]]:
                else:
                    stack.append(i)
            else:
                stack.append(i)
        #flushing the stack
        i = len(heights)
        while stack:
            cur = stack.pop()
            right = i-1
            left = stack[-1]+1 if stack else 0
            max_area = max(max_area, (right-left+1)*heights[cur])
        return max_area
        
        
        
        # Old
        # Time O(2n^2)
        # Space O(n^2)


        """
        n = len(heights)
        maxes = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            m = heights[i]
            for j in range(i, n):
                m = min(m, heights[j])
                maxes[i][j] = m
        result = 0
        for i in range(n):
            for j in range(i, n):
                result = max(result, (j-i+1)*maxes[i][j])
        return result
        """