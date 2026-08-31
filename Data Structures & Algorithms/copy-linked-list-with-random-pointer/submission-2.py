"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        dummy1=dummy2=newhead=Node(head.val)
        hashm={head:dummy1}
        idx=1
        head_dummy=head.next
        while head_dummy:
            dummy1.next=Node(head_dummy.val)
            hashm[head_dummy]=dummy1.next
            idx+=1
            dummy1,head_dummy=dummy1.next,head_dummy.next
        
        while head:
            if head.random:
                dummy2.random=hashm[head.random]
            head,dummy2=head.next,dummy2.next
        
        
        return newhead

        
