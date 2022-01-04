"""
leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

def lengthOfLongestSubstring(s):

    characterSet = set()
    result = 0
    left_ptr = 0

    for right_ptr in range(len(s)):
        # if letter already seen remove from left
        while s[right_ptr] in characterSet:
            characterSet.remove(s[left_ptr])
            left_ptr += 1
        
        characterSet.add(s[right_ptr])

        # length of sliding window
        result = max(right_ptr - left_ptr + 1, result)
    
    
    return result