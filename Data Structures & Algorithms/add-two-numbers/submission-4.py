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

        while dummy1 or dummy2 or carry:
            v1 = dummy1.val if dummy1 else 0
            v2 = dummy2.val if dummy2 else 0

            val = v1 +v2 + carry
            carry = val//10
            res = val%10
            dummy.next = ListNode(res)
            dummy = dummy.next
            dummy1 = dummy1.next if dummy1 else None
            dummy2 = dummy2.next if dummy2 else None
        
        return ans.next


