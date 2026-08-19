class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    # Initialize overall maximum, and current max/min to the first element
        global_max = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        
        for num in nums[1:]:
            # If the number is negative, multiplying flips signs:
            # the previous minimum becomes the candidate for maximum, and vice versa.
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            
            # Calculate new max and min ending at the current element
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            
            # Track the global maximum product seen so far
            global_max = max(global_max, cur_max)
            
        return global_max