"""
leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

def search(nums, target):
    try:
        return nums.index(target)
    except:
        return -1