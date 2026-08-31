# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        dummy=dummy2=head
        while dummy:
            dummy=dummy.next
            count+=1
        to_remove=count-n
        if to_remove==0:
            return head.next
        for i in range(to_remove-1):
            dummy2=dummy2.next
        dummy2.next=dummy2.next.next if dummy2.next else None
        return head