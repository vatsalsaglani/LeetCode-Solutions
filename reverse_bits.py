"""
leetcode: https://leetcode.com/problems/reverse-bits/
"""
def reverseBits(n):
    
    rep = list("{:032b}".format(n))
    rep.reverse()
    return int("".join(rep), 2)