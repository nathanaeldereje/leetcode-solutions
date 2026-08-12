# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums=[]
        def innerFunction(node):
            if not node:
                return
            # print(node.val)
            innerFunction(node.left)
            innerFunction(node.right)
            nums.append(node.val)
        innerFunction(root)
        return nums

