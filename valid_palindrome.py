"""
leetcode: https://leetcode.com/problems/valid-palindrome/
"""


def isPalindrome(s):

    s = [i for i in s.lower() if i.isalnum()]

    return True if s == s[::-1] else False