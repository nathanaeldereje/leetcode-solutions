"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        closed={}
        def innerFunction(node: Optional['Node']):
            if not node:
                return None
            if node in closed:
                return closed[node]
            copy=Node(node.val)
            closed[node]=copy
            for i in node.neighbors:
                copy.neighbors.append(innerFunction(i))
            return copy
        return(innerFunction(node))
  
        
