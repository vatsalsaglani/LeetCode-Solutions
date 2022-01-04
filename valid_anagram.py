"""
leetcode: https://leetcode.com/problems/valid-anagram/
"""

import collections

def isAnagram(s, t):

    start, target = collections.defaultdict(int), collections.defaultdict(int)

    for c in s:
        start[c] += 1
    
    for c in t:
        target[c] += 1
    
    return True if start == target else False