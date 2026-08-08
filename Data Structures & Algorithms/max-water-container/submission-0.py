class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(i,j):
            return abs(i-j)*min(heights[i], heights[j])
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, area(i,j))
            if heights[i] < heights [j]:
                i += 1
            else:
                j -= 1

        return max_area