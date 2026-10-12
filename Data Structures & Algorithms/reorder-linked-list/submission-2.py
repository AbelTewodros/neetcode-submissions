# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Get lenght of list
        slow,fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        curr = slow.next
        prev = slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second_list = prev
        initial_list = head

        while second_list and initial_list:
            temp = initial_list.next

            initial_list.next = second_list
            temp2 = second_list.next
            second_list.next = temp
            initial_list = temp
            second_list = temp2
        
        
        



