import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res={}
        intervals.sort()
        minheap=[]
        heapq.heapify(minheap)
        j=0
        
        for query in sorted(queries):
            while j<len(intervals) and query>=intervals[j][0]:
                total=intervals[j][1]-intervals[j][0]+1
                heapq.heappush(minheap,[total,intervals[j][1]])
                j+=1
            while minheap and minheap[0][1]<query:
                heapq.heappop(minheap)
            ans=minheap[0][0] if minheap else -1
            res[query]=ans
        return [res[i] for i in queries]

