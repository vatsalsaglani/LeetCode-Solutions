"""
leetcode: https://leetcode.com/problems/longest-consecutive-sequence/
"""


def longestConsecutive(nums):

    numSet = set(nums)
    longest = 0

    for number in nums:
        length = 0
        while number + length in numSet:
            length += 1
        longest = max(longest, length)

    return longest