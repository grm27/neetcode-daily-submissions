class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])

        res.append(intervals[0])

        for interval in intervals[1:]:
            last_interval = res[-1]
            if interval[0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], interval[1])
            else:
                res.append(interval)
        
        return res

