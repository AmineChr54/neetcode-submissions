class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        result = [intervals[0]]
        for s,e in intervals[1:]:
            last_end = result[-1][1]
            if s <= last_end:
                result[-1][1] = max(e, last_end)
            else:
                result.append([s,e])
        return result
        
        
        
        # REALLY BAD INTUITIVE SOLUTION:
        # OVERCOMPLICATED: O(N^2) Time, O(N) Space, unnecessary logic
        set_intervals = set()
        for x,y in intervals:
            set_intervals.add((x,y))

        """
        REPEAR UNTIL THE SET_INTERVAL IS EMPTY
        next_value = next(iter(set_intervals))
        set.intervals.remove(next_value)
        for interval in set_intervals:
            look for a interval that can be combined with it
            if found:
                delete it and add the combined after the loop ends i think so that it doesnt recheck it
            if not found any:
                result.append(next_value) 
        """

        def mix(a, b):
            if (b[0] <= a[1] and a[0] <= b[1]) or (a[0] <= b[1] and b[0] <= a[1]):
                return (min(a[0],b[0]), max(a[1],b[1])), True
            else:
                return None , False

        result = []
        while set_intervals:
            next_value = next(iter(set_intervals))
            set_intervals.remove(next_value)
            mixed_intervals = set()
            old_intervals = set()
            found = False
            for interval in set_intervals:
                val, cond = mix(interval, next_value)
                if cond:
                    mixed_intervals.add(val)
                    old_intervals.add(interval)
                    found = True
            if found:
                for old_interval in old_intervals:
                    set_intervals.remove(old_interval)
                for mixed_interval in mixed_intervals:
                    set_intervals.add(mixed_interval)
            else:
                result.append([next_value[0], next_value[1]])

        return result