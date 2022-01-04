"""
leetcode: https://leetcode.com/problems/reverse-linked-list/
"""

def reverseList(head):

    prev = None

    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    
    return prev