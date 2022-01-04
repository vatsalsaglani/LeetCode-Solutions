"""
leetcode: https://leetcode.com/problems/number-of-1-bits/
"""

from collections import Counter
# simiple solution
def hammingWeight(n):
    return Counter(bin(n)[2:])["1"]

# sol2
def hammingWeight(n):
    counter = 0
    while n:
        n = n & (n - 1)
        counter += 1
    
    return counter