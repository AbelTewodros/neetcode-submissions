from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ###We have tasks in ordered list, we want to kmow how many cycles
        ###it will take to finish in the least amount of time.
        ###We cant complete the same task until we get n in between
        ##Use a Max Heap to start with the biggest, then move to queue each time
        count=Counter(tasks)
        maxheap=[-c for c in count.values()]
        heapq.heapify(maxheap)
        time=0
        queue=deque()

        while maxheap or queue:
            time+=1
            if not maxheap:
                time=queue[0][1]
            else:
                curr=1+heapq.heappop(maxheap)
                if curr:
                    queue.append((curr,time+n))
            if queue and queue[0][1]==time:
                heapq.heappush(maxheap,queue.popleft()[0])
        return time

            

        