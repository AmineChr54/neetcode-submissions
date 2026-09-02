class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n = len(intervals)
        i = 0
        start, end = newInterval

        # 1. Skip non-overlapping intervals on the left
        while i < n and intervals[i][1] < start:
            i += 1
        
        left = i

        # 2. Absorb all overlapping intervals
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        
        right = i

        # 3. Replace the entire overlapping segment [left:right] in place
        intervals[left:right] = [[start, end]]

        return intervals