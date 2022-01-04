"""
leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):

    if not preorder or not inorder:
        return None
    
    # root from preorder
    root = TreeNode(preorder[0])
    # left and right from inorder
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])

    return root
