"""
leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

def levelOrder(root):

    if not root:
        return []
    traversal = []
    queue = []
    queue.append(root)

    while queue:
        loopLen = len(queue)
        level = []
        for i in range(loopLen):
            node = queue.pop(0)
            queue.append(node.left)
            queue.append(node.right)
            level.append(node.val)
        
        if level:
            traversal.append(level)
    
    return traversal
