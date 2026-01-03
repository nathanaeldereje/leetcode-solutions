# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        open=[]
        open.append(root)
        while(open):
            f=open.pop()
            f.left,f.right=f.right,f.left
            if f.left:
                open.append(f.left)
            if f.right:
                open.append(f.right)
        return root

            


        
