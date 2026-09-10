class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        summed = 0

        for i in range(len(nums)):
            summed += nums[i]

        return n*(n-1)//2 - summed