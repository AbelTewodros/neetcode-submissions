# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good=0
        maxi=root.val
       
        def dfs(root,maxi):
            nonlocal good

            if not root:
                 return
            good=good+1 if maxi<=root.val else good
            maxi=max(maxi,root.val)
            dfs(root.left,maxi)
            dfs(root.right,maxi)
       
        dfs(root,maxi)
        return good
            