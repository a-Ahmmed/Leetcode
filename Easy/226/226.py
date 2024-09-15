# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

 def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  # type: ignore
        
        def swapChildren(node):
            if node.left == None and node.right == None:
                return True

            node.left, node.right = node.right, node.left

            if node.left != None:
                swapChildren(node.left)
            
            if node.right != None:
                swapChildren(node.right)

        if root:
            swapChildren(root)

        return root