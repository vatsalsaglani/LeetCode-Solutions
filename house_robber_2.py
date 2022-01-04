"""
https://leetcode.com/problems/house-robber-ii/
"""

def rob(nums):



    def _rob(nums):

        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        
        return rob2

    
    return max(nums[0], _rob(nums[1:]), _rob(nums[:-1]))