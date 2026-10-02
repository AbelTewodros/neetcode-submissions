import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        heap_gift = [-i for i in gifts]
        heapq.heapify(heap_gift)

        for i in range(k):
            top = -1 * heapq.heappop(heap_gift)
            new_val = math.floor(math.sqrt(top))
            heapq.heappush(heap_gift,-1*new_val)
        heap_gift =[-1*h for h in heap_gift]
        return sum(heap_gift)