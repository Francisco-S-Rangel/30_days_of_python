from collections import deque
from typing import Deque, Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS (Breadth-First Search)
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_nodes: Deque[Tuple[Optional[TreeNode], Optional[TreeNode]]] = deque([(p, q)])
  
        while queue_nodes:
            current_p, current_q = queue_nodes.popleft()

            if current_p is None and current_q is None:
                continue
            
            if current_p is None or current_q is None:
                return False

            if current_p.val != current_q.val:
                return False

            queue_nodes.append((current_p.left, current_q.left))
            queue_nodes.append((current_p.right, current_q.right))
            
        return True

# DFS (Depth-First Search)
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
