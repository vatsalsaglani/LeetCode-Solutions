"""
leetcode: https://leetcode.com/problems/contains-duplicate/
"""

def containsDuplicate(nums):

    return not len(set(nums)) == len(nums)