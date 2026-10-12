# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        lenght = 0
        dummy = head

        while dummy:
            lenght += 1
            dummy = dummy.next
        
        deletion_zone = lenght - n

        if deletion_zone == 0:
            return head.next
        
        dummy = head
        idx = 0
        while dummy and idx < deletion_zone-1:
            dummy = dummy.next
            idx+=1
        dummy.next = dummy.next.next
        return head
        
        
