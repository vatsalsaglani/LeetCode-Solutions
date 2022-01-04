"""
leetcode: https://leetcode.com/problems/longest-increasing-subsequence/
"""

def lengthOfLIS(nums):

    # dp solution
    # start from end
    # eg, [2, 3] only one way to get LIS of 3 because there
    # are no numbers after that
    # for 2 it will be 1 + LIS(3) if 2 < 3 because it should
    # be in increasing order and as we start from back
    # the number before last must be lesser

    LIS = [1] * len(nums)
    # traversing from end
    # eg [2, 3, 4, 5]
    #.          i  j

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nus)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    
    return max(LIS)

    