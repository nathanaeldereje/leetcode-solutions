# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sumOfLeft=0
        open=deque([root])
        while open:
            f=open.popleft()

            if f.left:
                open.append(f.left)
                if  (not f.left.left and not f.left.right):
                    sumOfLeft+=f.left.val
            if f.right:
                open.append(f.right)
        return sumOfLeft
