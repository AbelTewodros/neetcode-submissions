import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]
        heapq.heapify(min_heap)
        for i in nums:
            heapq.heappush(min_heap,i)
            while len(min_heap)>k:
                heapq.heappop(min_heap)
        return min_heap[0]
        