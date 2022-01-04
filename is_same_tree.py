"""
leetcode: https://leetcode.com/problems/same-tree/
"""


def isSameTree(p, q):

    if not p and not q:
        return True

    elif not p or not q:
        return False

    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(
            p.right, q.right)
