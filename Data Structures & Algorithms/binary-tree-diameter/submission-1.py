# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left=self.longest(root.left)
        right=self.longest(root.right)
        return max(left+right,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
    
    def longest(self,root):
        if not root:
            return 0
        return 1+max(self.longest(root.left),self.longest(root.right))