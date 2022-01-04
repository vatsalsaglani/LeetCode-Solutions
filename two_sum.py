"""
leetcode: https://leetcode.com/problems/two-sum/
"""

def twoSum(nums, target):

    seen = {}

    for ix, num in enumerate(nums):
        if target - num in seen:
            return (seen[target-num],ix)
        
        seen[num] = ix
    
    