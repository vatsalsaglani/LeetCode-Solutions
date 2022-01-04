"""
https://leetcode.com/problems/validate-binary-search-tree/
"""

def isValidBST(root):

    def validate(node, left, right):

        if not node: return True

        if not (node.val < right.val and node.val > left.val): return False

        return (validate(node.left, node, node.val) and validate(node.right, node.val, right))

    return validate(root, float("-inf"), float("inf"))