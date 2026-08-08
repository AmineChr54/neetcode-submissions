class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0

        while i < j:
            h_i, h_j = heights[i], heights[j]
            h = min(h_i, h_j)
            
            # Direct calculation avoids function overhead
            area = (j - i) * h
            if area > max_area:
                max_area = area

            # Fast forward through lines that cannot produce a larger area
            if h_i <= h_j:
                while i < j and heights[i] <= h:
                    i += 1
            else:
                while i < j and heights[j] <= h:
                    j -= 1

        return max_area