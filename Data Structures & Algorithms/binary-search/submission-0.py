class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (r + 1 + l) // 2
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid

        if nums[l] == target:
                return l
        return -1


        """
        if len(nums)==0:
            return -1
        
        if nums[0] == target:
            return mid
        else 
        mid = nums[len(nums)//2]
        if target < mid:
            return self.search(nums[:mid], target)
        else:
            return self.search(nums[mid:], target)
        """