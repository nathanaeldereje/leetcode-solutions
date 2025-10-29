# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        check=False
        def innerFunction(node: Optional[TreeNode],sum,targetSum) -> int:
            if not node:
                return False
            if not node.left and not node.right:   
                    return sum+node.val == targetSum
            return (
                innerFunction(node.left, sum + node.val, targetSum) or
                innerFunction(node.right, sum + node.val, targetSum)
            )
            
        return innerFunction(root,0,targetSum)




