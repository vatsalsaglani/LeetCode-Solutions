"""
leetcode: https://leetcode.com/problems/palindromic-substrings/
"""


def countSubstrings(s):

    count = 0
    for i in range(len(s)):

        # odd length strings
        # eg. bab
        l, r = i, i

        while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        # even length strings
        # eg. baab
        l, r = i, i + 1

        while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

    
    return count