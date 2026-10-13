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
        
        
        #  Create a dictionary of every original node to a deep copy.
        dic_node = {None:None}
        dummy = head
        while dummy:
            dic_node[dummy] = Node(dummy.val)
            dummy = dummy.next
        
        #Go from the head to the end this time create the proper links
        dummy = head
        while dummy:
            curr_node = dic_node[dummy]
            curr_node.next = dic_node[dummy.next]
            curr_node.random = dic_node[dummy.random]
            dummy = dummy.next
        return dic_node[head]

        