import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       count=Counter(tasks)
       max_heap=[-c for c in count.values()]
       heapq.heapify(max_heap) #[-2,-2]
       
       queue=deque()#[-cnt,time]
       time=0
       while max_heap or queue:
            time+=1
            if not max_heap:
                time=queue[0][1]
            else:
                curr=1+heapq.heappop(max_heap)
                if curr:
                    queue.append([curr,time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(max_heap,queue.popleft()[0])
       return time
        



