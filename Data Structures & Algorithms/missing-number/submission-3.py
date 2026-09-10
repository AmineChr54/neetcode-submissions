class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing = missing ^ i ^ num
        return missing

        # mathetmatical
        n = len(nums)
        return n*(n+1)//2 - sum(nums)