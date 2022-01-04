"""
leetcode: https://leetcode.com/problems/valid-parentheses/
"""

def isValid(s):

    bracketMapping = {
        '(': ')',
        "{": "}",
        "[": "]"
    }
    bracketStack = []
    for bracket in s:
        if bracketMapping:
            bracketStack.append(bracket)
        else:
            if not bracketStack or bracketMapping[bracketStack.pop()] != bracket:
                return False
    
    return len(bracketStack) == 0