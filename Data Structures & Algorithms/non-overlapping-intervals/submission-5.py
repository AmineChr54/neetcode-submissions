class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort(key = lambda x : x[1])
        print(intervals)
        count = 0

        a = 0
        b = 1

        while b < len(intervals):
            if intervals[a][1] > intervals[b][0]:
                if intervals[a][1] >= intervals[b][1]:
                    a += 1
                    b += 1
                    count += 1
                else:
                    b += 1
                    count += 1
            else:
                a = b
                b += 1


        return count