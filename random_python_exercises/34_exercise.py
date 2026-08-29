from typing import Optional

class TreeNode:
    def __init__(self, val:int = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    root_stack: list[TreeNode] = []
    result: list[int] = []
    current_node: Optional[TreeNode] = root

    while current_node or root_stack:
        while current_node:
            root_stack.append(current_node)
            current_node = current_node.left

        current_node = root_stack.pop()
        result.append(current_node.val)

        current_node = current_node.right

    return result