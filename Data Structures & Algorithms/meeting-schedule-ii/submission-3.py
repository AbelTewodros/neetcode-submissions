"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_t = sorted(s.start for s in intervals)
        end_t = sorted(s.end for s in intervals)

        s_idx = end_idx = 0
        result = meeting_count = 0
        while s_idx < len(intervals):
            if start_t[s_idx] < end_t[end_idx]:
                meeting_count += 1
                result = max(meeting_count,result)
                s_idx += 1
            else:
                meeting_count -= 1
                end_idx += 1
        return result