# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Get lenght of list
        n = 0
        dummy = head
        while dummy:
            n+=1
            dummy = dummy.next
        #Get midpoint of list
        midpoint = (n//2)

        #Position to the start of the second list and then reverse
        second_list = dummy = head
        idx = 0
        while idx < midpoint:
            dummy = dummy.next
            idx +=1 
        
        temp = dummy.next
        dummy.next = None
        dummy = temp
        

        curr = dummy
        prev = None

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
        
        
        



