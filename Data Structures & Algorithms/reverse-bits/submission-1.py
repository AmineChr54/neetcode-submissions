class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            last_bit = n & 1
            last_bit_at_the_end = (last_bit << (32 - i - 1))
            n = n >> 1
            result += last_bit_at_the_end
            print(f"{result:b}")
        return result