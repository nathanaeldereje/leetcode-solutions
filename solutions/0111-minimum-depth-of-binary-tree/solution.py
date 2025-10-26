# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left, right = root.left, root.right
        if not left:
            return 1 + self.minDepth(right)
        if not right:
            return 1 + self.minDepth(left)
        return 1 + min(self.minDepth(left), self.minDepth(right))


