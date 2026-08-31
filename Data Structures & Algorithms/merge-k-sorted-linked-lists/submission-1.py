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
        while total>0:
            total=len(lists)-1
            curr=float('inf')
            for i in range(len(lists)):
                if not lists[i]:
                    total-=1
                elif lists[i].val<curr:
                        curr,to_move=lists[i].val,i
            res.next=lists[to_move]
            lists[to_move],res=lists[to_move].next,res.next
        return dummy.next
            
            

            
