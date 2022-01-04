"""
leetcode: https://leetcode.com/problems/product-of-array-except-self/
"""


def productExceptions(nums):

    # left product
    prod_left = [1] * len(nums)

    for i in range(1, len(nums)):
        prod_left[i] = prod_left[i - 1] * nums[i - 1]

    # right product
    prod_right = [1] * len(nums)
    for i in range(len(nums)-2, -1, -1):
        prod_right[i] = prod_right[i-1] * nums[i-1]
    
    res = [1] * len(nums)
    for i in range(len(nums)):
        res[i] = prod_left[i] * prod_right[i]
    
    return res
    