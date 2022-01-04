"""
leetcode: https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


def maxPathSum(root):

    max_sum = root.val

    def calculateMax(node):

        if not node:
            return 0

        l = calculateMax(node.left)
        r = calculateMax(node.right)

        max_sum = max(max_sum, node.val, node.val + l, node.val + r,
                      node.val + l + r)

        return max(node.val, node.val + l, node.val + r)
    
    calculateMax(root)
    
    return max_sum
