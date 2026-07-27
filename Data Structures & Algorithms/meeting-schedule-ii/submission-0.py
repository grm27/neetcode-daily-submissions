"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])
        res = i = j = 0        
        rooms = 0

        while i < n and j < n:
            if start[i] < end[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            res = max(res, rooms)
    
        return res
            