"""
leetcode: https://leetcode.com/problems/sum-of-two-integers/
"""

# mug this solution

def getSum(a, b):
    carry = 0
    mask = 0xffffffff
    while b & mask != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    
    return a&mask if b > mask else a
