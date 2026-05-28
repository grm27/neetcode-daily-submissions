class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])

        res.append(intervals[0])

        for start, end in intervals[1:]:
            last_interval = res[-1]
            if start <= last_interval[1]:
                last_interval[1] = max(last_interval[1], end)
            else:
                res.append([start, end])
        
        return res

