class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int: # type: ignore
        def longest(root: TreeNode) -> int:
            if not root:
                return 0
            
            return 1 + max([longest(root.left), longest(root.right)])
        
        return longest(root) if root else 0
