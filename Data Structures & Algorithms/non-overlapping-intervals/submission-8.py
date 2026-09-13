class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removed_count = 0
        curr = intervals[0]
        idx = 1
        n = len(intervals)

        while idx < n:
            if curr[-1] > intervals[idx][0]:
                removed_count += 1
                curr = intervals[idx] if curr[1]>intervals[idx][1] else curr
            else:
                curr = intervals[idx]
            
            idx += 1
        return removed_count