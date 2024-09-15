# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # type: ignore
    def diameter(node: TreeNode, store: list = [0]):
        if not node:
            return 0

        l = diameter(node.left, store)
        r = diameter(node.right, store)

        if l + r > store[0]:
            store[0] = l + r

        return 1 + l if l > r else 1 + r

    store = [0]
    diameter(root, store)
    return store[0]