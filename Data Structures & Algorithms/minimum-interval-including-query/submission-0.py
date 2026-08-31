import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minheap,res=[],{}
        heapq.heapify(minheap)
        intervals.sort(key=lambda x:x[0])
        i=0
        for j in sorted(queries):
            while i<len(intervals) and intervals[i][0]<=j:
                size=intervals[i][1]-intervals[i][0]+1
                heapq.heappush(minheap,[size,intervals[i][1]])
                i+=1
            while minheap and minheap[0][1]<j:
                heapq.heappop(minheap)
            if not minheap:
                res[j]=-1
            else:
                res[j]=minheap[0][0]
        return [res[j] for j in queries]

