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
        counter=0
        q=deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                current=q.popleft()
                if current.left: q.append(current.left)
                if current.right: q.append(current.right)
            counter+=1
            
        return counter

