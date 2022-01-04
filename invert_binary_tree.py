"""
leetcode: https://leetcode.com/problems/invert-binary-tree/
"""

def invertTree(root):

    if root:

        root.left, root.right = root.right, root.left

        # invert left and right subtree

        if root.left:

            invertTree(root.left)
        
        if root.right:

            invertTree(root.right)
        
        return root
    
    else:

        return None