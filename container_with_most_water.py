"""
leetcode: https://leetcode.com/problems/container-with-most-water/
"""


def maxArea(heights):

    left_ptr = 0
    right_ptr = len(heights) - 1
    max_area = 0

    while left_ptr < right_ptr:
        max_area = max(max_area, (right_ptr - left_ptr) * min(heights[left_ptr], heights[right_ptr]))
        
        # move right towards left if height at right is lesser than height at left
        if heights[left_ptr] > heights[right_ptr]:
            right_ptr -= 1
        # move left towards right if height at right is greater than height at left
        elif heights[left_ptr] < heights[right_ptr]:
            left_ptr += 1
        
        else:
            # can update any can do right -= 1
            left_ptr += 1
    
    return max_area