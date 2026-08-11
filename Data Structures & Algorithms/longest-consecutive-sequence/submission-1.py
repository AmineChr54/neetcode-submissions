class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_seq = 0

        while set_nums:
            cur_num = set_nums.pop()
        
            cur_seq = 1 
            up = cur_num + 1
            down = cur_num - 1
        
            while up in set_nums:
                set_nums.remove(up)
                up += 1
                cur_seq += 1
            while down in set_nums:
                set_nums.remove(down)
                down -= 1
                cur_seq += 1
        
            max_seq = max(max_seq, cur_seq)
        return max_seq