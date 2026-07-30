class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nzeros = len([num for num in nums if num == 0])
        if nzeros > 1:
            print("case1")
            return [0]*len(nums)

        if nzeros == 1:
            print("case2")
            result = [0]*len(nums)
            p = 1
            pind = 0
            for i in range(len(nums)):
                if nums[i]==0:
                    pind = i
                else:
                    p*=nums[i]
            result[pind] = p
            return result
            
        else:
            print("case3")
            p=1
            for num in nums:
                p*=num
            return [p//num for num in nums]