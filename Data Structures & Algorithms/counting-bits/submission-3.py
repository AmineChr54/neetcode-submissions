class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        result = [0]
        for i in range(1, n+1):
            cur = i
            cur = cur & (cur - 1)
            count = result[cur] + 1
            result.append(count)
        return result