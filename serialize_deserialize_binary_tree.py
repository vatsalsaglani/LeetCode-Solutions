"""
leetcode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):

        flat_bt = []
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node:
                flat_bt.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                flat_bt.append("")
        
        return ",".join(flat_bt)
    
    def deserialize(self, data):

        if not data:
            return
        
        flat_bt = data.split(",")
        root = TreeNode(flat_bt[0])
        queue = []
        queue.append(root)
        i = 1
        while queue:
            node = queue.pop(0)
            if i < len(flat_bt) and flat_bt[i]:
                node.left = TreeNode(int(flat_bt[i]))
                queue.append(node.left)
            i += 1
            if i < len(flat_bt) and flat_bt[i]:
                node.right = TreeNode(int(flat_bt[i]))
                queue.append(node.right)
            i += 1
        
        return root
            