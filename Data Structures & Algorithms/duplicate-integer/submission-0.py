class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i, num in enumerate(nums):
            if str(num) in map:
                return True
            else:
                map[str(num)] = 1
        return False
