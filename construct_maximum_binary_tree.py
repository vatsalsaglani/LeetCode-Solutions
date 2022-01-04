class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):

    if not nums:

        return None

    max_num = max(nums)

    root = TreeNode(max_num)

    mid = nums.index(max_num)

    left = nums[:mid]

    right = nums[mid+1:]

    root.left = constructMaximumBinaryTree(left)

    root.right = constructMaximumBinaryTree(right)

    return root