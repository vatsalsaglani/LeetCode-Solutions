"""
leetcode: https://leetcode.com/problems/group-anagrams/
"""
from collections import defaultdict

def groupAnagrams(strs):

    groups = defaultdict(list)

    for st in strs:
        s = "".join(sorted(st))
        groups[s].append[st]

    return [v for v in groups.values()]