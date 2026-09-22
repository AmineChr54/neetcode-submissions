class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row
        l = 0
        r = len(matrix) - 1
        while l < r:
            m = (l + r + 1) // 2
            if target < matrix[m][0]:
                r = m - 1
            else:
                l = m
        # search the value in the found row
        row = l
        l = 0
        r = len(matrix[row]) - 1
        while l < r:
            m = (l + r + 1) // 2
            if target < matrix[row][m]:
                r = m - 1
            else:
                l = m

        if matrix[row][l] == target:
            return True
        return False

