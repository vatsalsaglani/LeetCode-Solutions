"""
leetcode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

def kthSmallest(root, k):

    n = 0
    current = root
    stack = []

    while current or stack:
        # left sub tree current
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        n += 1
        if n == k:
            return current.val
        
        # right subtree in currents
        current = current.right