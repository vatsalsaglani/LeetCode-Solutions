"""
leetcode: https://leetcode.com/problems/longest-palindromic-substring/
"""

def longestPalindrome(s):

    res, resLen = "", 0

    for i in range(len(s)):
        
        
        # odd length strings
        # eg. bab
        l, r =  i, i

        while 0<=l<len(s) and 0<=r<len(s) and s[l]==s[r]:

            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            
            l -= 1
            r += 1
        
        # even length strings
        # eg, baab
        l, r =  i, i+1

        while 0<=l<len(s) and 0<=r<len(s) and s[l]==s[r]:

            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            
            l -= 1
            r += 1
    
    return res