import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap=[]
        heapq.heapify(min_heap)
        for i in stones:
            heapq.heappush(min_heap,-i)
        while len(min_heap)>1:
            x=-1*heapq.heappop(min_heap)
            y=-1*heapq.heappop(min_heap)
            res=abs(x-y)
            heapq.heappush(min_heap,-res)
        return -min_heap[0] if len(min_heap) else 0