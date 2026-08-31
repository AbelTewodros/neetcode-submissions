# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lowest=root
        while lowest:
            if lowest.val>p.val and lowest.val>q.val:
                lowest=lowest.left
            elif lowest.val<p.val and lowest.val<q.val:
                lowest=lowest.right
            else:
                return lowest
