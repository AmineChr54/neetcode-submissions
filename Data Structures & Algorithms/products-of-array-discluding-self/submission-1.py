class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixarray = [1]*len(nums)
        suffixarray = [1]*len(nums)

        ppre = 1
        for i in range(len(nums)):
            # we can check if nums[i] = 0 to save some work
            ppre *= nums[i]
            prefixarray[i] = ppre

        psuf = 1
        for i in range(len(nums)-1, -1, -1):
            # we can check if nums[i] = 0 to save some work
            psuf *= nums[i]
            suffixarray[i] = psuf

        print(prefixarray)
        print(suffixarray)
  
        result = nums
        result = [suffixarray[1]] + [prefixarray[i-1] * suffixarray[i+1] for i in range(1, len(nums)-1)] + [prefixarray[-2]]

        return result