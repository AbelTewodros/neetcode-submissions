# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        curr=False
        if not root and not subRoot:
            return True
        elif root and subRoot and root.val==subRoot.val:
            curr=self.checkTree(root,subRoot)
        while root and curr is False:
            curr=self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            break
        return curr
      
    def checkTree(self,root,subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val==subRoot.val:
                return self.checkTree(root.left,subRoot.left) and self.checkTree(root.right,subRoot.right)
            return False



