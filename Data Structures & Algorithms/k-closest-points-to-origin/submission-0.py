import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ##Basically we want to create a heap for the distances 
        ##but we want to link each node to a coordinate. So make
        ##a heap using a tuple to have the distance then the idx.
        min_heap=[]
        res=[]
        heapq.heapify(min_heap)
        for i in range(len(points)):
            distance=((points[i][0])**2 +(points[i][1])**2)
            heapq.heappush(min_heap,(distance,i))
        for i in range(k):
            idx=heapq.heappop(min_heap)[1]
            res.append(points[idx])
        return res