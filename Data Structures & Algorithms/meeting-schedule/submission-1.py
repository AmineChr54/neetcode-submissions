"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key= lambda x: x.start)

        last_end = intervals[0].end
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            if last_end <= start:
                last_end = end
            else:
                return False
        return True