"""
leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/
"""

def lowestCommonAncestor(root, p, q):

    if not root:
        return None
    
    if root.val == p.val or root.val == q.val:
        return root
    
    left_sub = lowestCommonAncestor(root.left, p, q)
    right_sub = lowestCommonAncestor(root.right, p, q)

    if not left_sub:
        return right_sub
    if not right_sub:
        return left_sub

    # if no returns get executed return the root
    return root

