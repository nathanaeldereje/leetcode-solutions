# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def innerFunction(node: Optional[TreeNode]):
            if not node:
                return
            # Left subtree
            innerFunction(node.left)
            # Root
            res.append(node.val)
            # Right subtree
            innerFunction(node.right)

        innerFunction(root)
        return res
