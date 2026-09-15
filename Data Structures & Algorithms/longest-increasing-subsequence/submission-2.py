class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


        # False logic as well
        sets = []
        sets.append([nums[-1], nums[-1], 1]) # min max len
        for i in range(len(nums)-2, -1, -1):
            inserted = False
            for s in sets:
                if nums[i] < s[0]:
                    s[0] = nums[i]
                    s[2] += 1
                    inserted = True
            if not inserted:
                sets.append([nums[i], nums[i], 1])
        max_len = 0
        for s in sets:
            if s[2] > max_len:
                max_len = s[2]
        return max_len
                


        # completely false logic
        max_len = 0
        for i in range(len(nums)-1):
            cur_len = 1
            cur_max_e = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > cur_max_e:
                    cur_max_e = nums[j]
                    cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len