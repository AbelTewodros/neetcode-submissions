class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removed_count = 0

        curr = intervals[0]
        idx = 1
        while idx < len(intervals):
            if curr[1] > intervals[idx][0]: 
                removed_count += 1
                if curr[1] > intervals[idx][1]:
                    curr = intervals[idx]
            else:
                curr = intervals[idx]
            idx += 1
        return removed_count
