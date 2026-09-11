class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            count = 0
            cur = i
            while cur != 0:
                cur = cur & (cur - 1)
                count += 1
            result.append(count)
        return result