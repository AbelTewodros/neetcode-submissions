import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        heapq.heapify(self.maxheap)
        self.minheap=[]
        heapq.heapify(self.minheap)


    def addNum(self, num: int) -> None:
        if not self.minheap and not self.maxheap:
            heapq.heappush(self.maxheap,-num)
        else:
            if self.maxheap and -num<self.maxheap[0]:
                heapq.heappush(self.minheap,num)
            else:
                heapq.heappush(self.maxheap,-num)
        diff=abs(len(self.minheap)-len(self.maxheap))
        if diff>1:
            if len(self.minheap)>len(self.maxheap):
                current=-heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap,current)
            else:
                current=-heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap,current)
            

    def findMedian(self) -> float:
        total=len(self.minheap)+len(self.maxheap)
        if not total:
            return 0
        elif total%2!=0:
            if len(self.maxheap)==((total)//2)+1:
                return -self.maxheap[0]
            else:
                return self.minheap[0]
        if self.maxheap and self.minheap:
            return (-self.maxheap[0]+ self.minheap[0])/2
        if not self.minheap:
            return (-self.maxheap[0]+(-self.maxheap[1]))/2
        return (self.minheap[0]+self.minheap[1])/2
        
        
        