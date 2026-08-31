# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
        second=slow.next
        slow.next=None

        prev=None
        while second:
            cur=second.next
            second.next=prev
            prev=second
            second=cur
        
        while prev:
            temp1,temp2=head.next,prev.next
            head.next=prev
            prev.next=temp1
            prev=temp2
            head=temp1

        
        
        


