class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ###Are the intervals sorted? No that means we cant go 1 by 1.
        ###If we sort that would lead us to logn time average case if we do the sort in place
        ###Once sorted by starting value we know that there is an overlap if the second value of 
        ###the current list is > than the first value or smaller than the second value. So we
        ###can take the smallest value for left between current and next and take the biggest between
        ### current and next
        ###We can add to a new list instead of editing curent as that would cause complexity issues
        intervals.sort()
        res=[]
        curr=intervals[0]
        for i in range(1,len(intervals)):
            if curr[1]>= intervals[i][0]:
                curr=[min(curr[0],intervals[i][0]),max(curr[1],intervals[i][1])]
            else:
                res.append(curr)
                curr=intervals[i]
        res.append(curr)
        return res
