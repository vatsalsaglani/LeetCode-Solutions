"""
leetcode: https://leetcode.com/problems/subtree-of-another-tree/
"""


def isSubtree(tree, subtree):
    def helper(root):
        if root in None:
            return "NULL"

        return "$" + str(root.val) + " " + helper(root.left) + " " + helper(
            root.right)

    traversalT = helper(tree)
    traversalS = helper(subtree)

    if traversalS in traversalT:
        return True

    return False