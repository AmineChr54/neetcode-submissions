from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        def multiply(A, B):
            return [
                [
                    A[0][0] * B[0][0] + A[0][1] * B[1][0],
                    A[0][0] * B[0][1] + A[0][1] * B[1][1],
                ],
                [
                    A[1][0] * B[0][0] + A[1][1] * B[1][0],
                    A[1][0] * B[0][1] + A[1][1] * B[1][1],
                ],
            ]

        def matrix_pow(mat, p):
            res = [[1, 0], [0, 1]]  # Identity matrix
            base = mat
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        T = [[1, 1], [1, 0]]
        res = matrix_pow(T, n)
        return res[0][0]

"""
        @lru_cache(maxsize=None)
        def dp(n):
            if n<=3:
                return n
            return dp(n-1) + dp(n-2) 
        
        return dp(n)"""
                