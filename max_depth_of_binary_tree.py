"""
leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

def maxDepth(root):

    if not root:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return max(left_depth, right_depth) + 1