"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def postorder(node):
            if node is None:
                return node
            
            for child in node.children:
                postorder(child)
            
            result.append(node.val)
        
        postorder(root)
        return result