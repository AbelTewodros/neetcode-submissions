import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = nums[0:k]
        for i in range(len(heap)):
            heap[i] *= -1
            heap[i] = (heap[i],i)
        heapq.heapify(heap)

        res = []
        res.append(heap[0][0]*-1)

        left = 1
        for i in range(k,len(nums)):
            while heap and (heap[0][1] < left or heap[0][1]>i):
                heapq.heappop(heap)
            heapq.heappush(heap,(nums[i]*-1,i))
            res.append(heap[0][0]*-1)
            left += 1
        return res
