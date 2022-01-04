"""
leetcode: https://leetcode.com/problems/longest-repeating-character-replacement/
"""

## mug it up

import collections

def characterReplacement(s, k):

    freqDict = collections.defaultdict(int)
    maxFreq = 0
    maxLen = 0
    start = 0
    end = 0

    while end < len(s):

        freqDict[s[end]] += 1

        maxFreq = max(maxFreq, freqDict[s[end]])

        if ((end - start + 1) - maxFreq) > k:

            freqDict[s[start]] -= 1
            start += 1
        
        else:
            maxLen = max(maxLen, end - start + 1)
        
        end += 1
    
    return maxLen
