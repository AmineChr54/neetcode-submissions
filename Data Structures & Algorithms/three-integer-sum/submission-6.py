class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Optimization 1: If smallest remaining number is > 0, sum can never be 0
            if nums[i] > 0:
                break

            # Skip duplicates for the anchor element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Optimization 2: Fast-forward if maximum possible sum with this anchor is still < 0
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            l, r = i + 1, n - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicates for left and right pointers
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1

        return result