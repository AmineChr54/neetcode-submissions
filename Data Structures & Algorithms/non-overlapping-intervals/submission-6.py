class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort(key = lambda x : x[1])

        count = 0
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start,end = intervals[i]
            if start < last_end:
                count += 1
            else:
                last_end = end
        return count 




        # old solution
        intervals.sort(key = lambda x : x[1])
        
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