class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        ###[1,2][3,6]
        ###compare: output=[1,2][3,6]
        ####how do we know that [1,4] is an overlap of [1,2]? Well the smaller value in output
        #### is smaller than the bigger value of current, and vice versa. So since this is true we can 
        ###just not append it to output and continue. Then is 2>=2 yes. so its not going to overlap we can ad

        intervals.sort()
        end=intervals[0][1]
        count=0
        for start,new_end in intervals[1:]:
            if start>=end:
                end=max(end,new_end)
            else:
                count+=1
                end=min(end,new_end)
        return count
