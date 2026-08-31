"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
So I have to create a node then the next node and the next.
The idea could be depth first search. Well we first clone the node
we are at Then we clone the children and add it to neighbors.
Seems recursive.
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
     
        hash={}
        def dfs(node):
            if node in hash:
                return hash[node]
            
            new_node=Node(node.val)
            hash[node]=new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        
        return dfs(node) if node else None

        
            


        