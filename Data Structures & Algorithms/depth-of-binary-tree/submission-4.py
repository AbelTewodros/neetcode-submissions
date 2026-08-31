# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxi=0
        stack=[]
        stack.append((root,1))
        while stack:
            
                current,depth=stack.pop()
                maxi=max(maxi,depth)
                if current.right:stack.append((current.right,depth+1))
                if current.left:stack.append((current.left,depth+1))
        return maxi


