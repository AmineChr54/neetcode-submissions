class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []

        def backtrack(start):
            result.append(path[:])               # every node of the decision tree is a valid subset
            for i in range(start, len(nums)):
                path.append(nums[i])             # choose
                backtrack(i + 1)                 # explore: only elements to the right may follow
                path.pop()                       # unchoose
        
        backtrack(0)
        return result