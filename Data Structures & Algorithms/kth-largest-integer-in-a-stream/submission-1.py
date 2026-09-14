import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        
        ##Make sure heap is always of length k
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]