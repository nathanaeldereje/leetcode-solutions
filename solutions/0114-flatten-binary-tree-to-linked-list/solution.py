# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        open = [root]
        prev=None

        while open:
            current = open.pop()
            print(current.val)
            if current.right:
                open.append(current.right)

            if current.left:
                open.append(current.left)
            if prev:
                prev.right=current
                prev.left=None
            prev=current
            

        


            
