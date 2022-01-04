"""
leetcode: https://leetcode.com/problems/jump-game/
"""

def canJump(nums):

    if len(nums) == 1:
        return True
    limit = nums[0]
    if limit == 0:
        return False
    for i in range(len(nums)-1):
        if i > limit:
            break
        limit = max(limit, i + nums[i])
        if limit >= len(nums) - 1:
            return True
    
    return False