class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        current_path = []
        result = []
        def backtrack(i, remaining):
            if remaining == 0:
                result.append(current_path.copy())
                return
            if remaining < 0 or i == len(nums):
                return

            # Choose
            current_path.append(nums[i])
            backtrack(i, remaining - nums[i])
            current_path.pop()
            # Skip
            backtrack(i+1, remaining)




        backtrack(0, target)
        return result