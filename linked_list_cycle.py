"""
leetcode: https://leetcode.com/problems/linked-list-cycle/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):

    visited = set()
    while head:
        if not head in visited:
            visited.add(head)
        else: return True
        head = head.next
    
    return False


def hasCycle(head):
    while head:
        if head.val == 'v':
            return True
        head.val = "v"

        head = head.next
    
    return False