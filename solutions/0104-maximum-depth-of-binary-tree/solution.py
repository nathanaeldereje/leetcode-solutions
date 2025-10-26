# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def innerFunction(node: Optional[TreeNode],count):
            if not node:
                return count
            left=innerFunction(node.left,count+1)
            right =innerFunction(node.right,count+1)
            return max(left,right)

        return innerFunction(root,0)
