# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums=[]
        def innerFunction(node):
            if not node:
                return
            print(node.val)
            nums.append(node.val)
            innerFunction(node.left)
            innerFunction(node.right)
        innerFunction(root)
        return nums
