# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(self, root: Optional[TreeNode]) -> bool: # type: ignore
        def height(node: TreeNode):
            if not node:
                return 0

            return 1 + max([height(node.left), height(node.right)])

        def balanced(root: TreeNode):
            if not root:
                return True

            if abs(height(root.left) - height(root.right)) <= 1:
                return all(i == True for i in [balanced(root.left), balanced(root.right)])
            else:
                return False
            
        return balanced(root) if root else True