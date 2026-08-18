
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for k in range(n // 2):
            for i in range(k, n - k - 1):
                (matrix[k][i], 
                matrix[i][n - k -1], 
                matrix[n - k - 1][n - i - 1], 
                matrix[n - i - 1][k]
                ) = (
                    matrix[n - i - 1][k],
                    matrix[k][i],
                    matrix[i][n-k-1],
                    matrix[n - k - 1][n - i - 1],
                )