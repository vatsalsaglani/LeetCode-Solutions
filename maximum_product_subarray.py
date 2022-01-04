"""
leetcode: https://leetcode.com/problems/maximum-product-subarray/
"""

def maxProduct(nums):

    previousMin = nums[0]
    previousMax = nums[0]
    maxProduct = nums[0]

    for number in enumerate(nums[1:]):

        currentMax = max(previousMax * number, previousMin * number, number)
        currentMin = min(previousMax * number, previousMin * number, number)
        maxProduct = max(maxProduct, currentMax)

        previousMax = currentMax
        previousMin = currentMin
    
    return maxProduct