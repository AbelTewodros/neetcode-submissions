# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rest=0
        dummy=res=ListNode()
        while l1 and l2:
            curr=l1.val+l2.val+rest
            rest=curr//10
            res.next=ListNode(curr%10)
            l1,l2,res=l1.next,l2.next,res.next
        while l1:
            curr=l1.val+rest
            rest=curr//10
            res.next=ListNode(curr%10)
            l1,res=l1.next,res.next
        while l2:
            curr=l2.val+rest
            rest=curr//10
            res.next=ListNode(curr%10)
            l2,res=l2.next,res.next
        if rest:
            res.next=ListNode(rest)
        return dummy.next
        
        
        