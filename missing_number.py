"""
leetcode: https://leetcode.com/problems/missing-number/
"""

def missingNumber(nums):
    maxNum = len(nums)
    n = [i for i in range(maxNum+1) if not i in nums]
    return n[0]
