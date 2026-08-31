# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lowest=root
        def dfs(root):
            nonlocal p,q,lowest
            if root.val==p.val or root.val==q.val:
                return root
            
            if root.val>p.val and root.val>q.val:
                lowest=root
                return dfs(root.left)
            elif root.val<p.val and root.val<q.val:
                lowest=root
                return dfs(root.right)
            else:
                return root
        return dfs(root)
