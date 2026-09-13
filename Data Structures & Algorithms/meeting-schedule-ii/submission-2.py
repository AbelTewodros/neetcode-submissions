"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])
        
        s,e = 0,0
        count = 0
        res = 1

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                res = max(count,res)
                s += 1
            else:
                count -=1
                e += 1
        return res
