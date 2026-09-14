import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []


    def addNum(self, num: int) -> None:
        if self.max_heap and num < -1 * self.max_heap[0]:
             heapq.heappush(self.max_heap, -1 * num)

        else:
            heapq.heappush(self.min_heap,num)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
       

    def findMedian(self) -> float:
        total_len = len(self.min_heap) + len(self.max_heap)
        if total_len % 2 == 0:
            return ((-1*self.max_heap[0]) + self.min_heap[0])/2
        return  self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else -self.max_heap[0]
        
        
        