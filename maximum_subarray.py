"""
leetcode: https://leetcode.com/problems/maximum-subarray/
"""

def maxSubArray(nums):

    if len(nums) == 1:
        return nums[0]
    
    currentSum = nums[0]
    maxSum = nums[0]
    for ix, number in enumerate(nums[1:]):
        currentSum = max(number, currentSum + number)
        maxSum = max(currentSum, maxSum)
    
    return maxSum