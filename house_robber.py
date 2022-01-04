"""
leetcode: https://leetcode.com/problems/house-robber/
"""

def rob(nums):

    rob1, rob2 = 0, 0

    for n in nums:
        newRob = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = newRob
    
    return rob2