# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited,ind={},0
        while head:
            if head.val in visited:
                return True 
            visited[head.val]=ind
            ind+=1
            head=head.next
        return False