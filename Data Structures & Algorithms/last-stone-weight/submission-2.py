import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap=[]
        heapq.heapify(min_heap)
        #Complexity is N being the lenght of Stones.
        for i in stones:
            heapq.heappush(min_heap,-i)
        while len(min_heap)>1:
            x=heapq.heappop(min_heap)
            y=heapq.heappop(min_heap)
            res=x-y
            if res==0:
                continue
            heapq.heappush(min_heap,res)
        return -min_heap[0] if len(min_heap) else 0