# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs_h(root,h=0):
            nonlocal l
            if not root:
                return
            to_add=[[root.val,h]]
            l.extend(to_add)
            dfs_h(root.left,h+1)
            dfs_h(root.right,h+1)
            return l
            
        l=[]
        if not root:
            return []
        dfs_h(root)
        to_return=[]

        for i in l:
            if i[1]>=len(to_return):
                to_return.append([i[0]])
            else:
                to_return[i[1]].append(i[0])
        return to_return                
    
    
    


        
        
            