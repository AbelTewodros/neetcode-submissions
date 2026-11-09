# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ans = ListNode()
        dummy = ans
        curr_heap = [(lists[l].val, l, lists[l]) for l in range(len(lists)) if lists[l] is not None]

        heapq.heapify(curr_heap)

        while curr_heap:
            val,list_idx,curr_pointer = heapq.heappop(curr_heap)
            dummy.next = ListNode(val)
            curr_pointer = curr_pointer.next
            if curr_pointer:
                heapq.heappush(curr_heap,(curr_pointer.val,list_idx,curr_pointer))
            dummy = dummy.next

        return ans.next