"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        open = deque([root])
        while open:
            prev = None        
            size=len(open)
            for i in range(size):
                x=open.popleft()
                if prev:
                    prev.next = x
                prev = x
                if x.left:
                    open.append(x.left)
                if x.right:
                    open.append(x.right)
            
        return root
        
