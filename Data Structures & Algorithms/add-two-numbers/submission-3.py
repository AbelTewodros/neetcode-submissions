# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = dummy = ListNode()

        dummy1 = l1
        dummy2 = l2
        carry = 0

        while dummy1 and dummy2:
            res = dummy1.val + dummy2.val + carry
            carry = 0
            if res >= 10:
                carry = res//10
                res%=10
            dummy.next = ListNode(res)
            dummy = dummy.next
            dummy1,dummy2 = dummy1.next,dummy2.next
        
        while dummy1:
            res = dummy1.val + carry
            carry = 0
            if res >= 10:
                carry = res//10
                res%=10
            dummy.next = ListNode(res)
            dummy = dummy.next
            dummy1 = dummy1.next
        
        while dummy2:
            res = dummy2.val + carry
            carry = 0
            if res >= 10:
                carry = res//10
                res%=10
            dummy.next = ListNode(res)
            dummy = dummy.next
            dummy2 = dummy2.next

        if carry != 0 :
            dummy.next = ListNode(carry)
        
        return ans.next
