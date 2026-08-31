# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=dummy=ListNode()
        to_move=None
        total=len(lists)
        while True:
            curr=float('inf')
            for i in range(len(lists)):
                if lists[i] and lists[i].val<curr:
                        curr,to_move=lists[i].val,i
            if curr==float('inf'):
                break
            res.next=lists[to_move]
            lists[to_move],res=lists[to_move].next,res.next
        return dummy.next
            
            

            
