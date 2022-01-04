"""
leetcode: https://leetcode.com/problems/counting-bits/
"""
from collections import Counter
# pythonic
def countBits(num):
    op = [0]
    for i in (1, num + 1):
        op.append(Counter(bin(i)[2:])["1"])
    
    return op

# logical pattern

def countBits(num):
    op = [0]
    while len(op) <= num:
        op.extend([i+1 for i in op])
    
    return op[:num+1]
