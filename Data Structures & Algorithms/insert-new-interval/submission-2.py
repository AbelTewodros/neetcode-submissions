class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output=[]
        i=0
        n=len(intervals)
        
        while i<n and newInterval[0]>intervals[i][1]:
            output.append(intervals[i])
            i+=1

        while i<n and newInterval[1]>=intervals[i][0]:
            newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
            i+=1
        output.append(newInterval)  
        while i<n:
            output.append(intervals[i])    
            i+=1  
                
             
        return output      

            

