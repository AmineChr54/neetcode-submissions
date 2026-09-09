class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        i = 0
        while i <= max_reach < len(nums) - 1:
            max_reach = max(max_reach, i + nums[i])
            i += 1
        if max_reach >= len(nums) -1:
            return True
        else:
            return False

        

        # dp appreach, not so good
        self.reached = False
        def dp(i):
            if i >= len(nums) - 1:
                self.reached = True
                return 
            if nums[i] == 0:
                return 

            j = nums[i]
            while j > 0 and self.reached == False:
                dp(i + j)
                j -= 1
            return

        dp(0)
        return self.reached