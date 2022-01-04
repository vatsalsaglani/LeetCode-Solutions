"""
leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

def lowestCommonAncestor(root, p, q):

    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    
    elif q.val > root.val and p.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    
    else:
        return root
