# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        open = deque([root])
        result = deque()

        while open:
            level_size = len(open)  # number of nodes at current level
            level_nodes = []

            for _ in range(level_size):
                node = open.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    open.append(node.left)
                if node.right:
                    open.append(node.right)

            result.appendleft(level_nodes)

        return list(result)
