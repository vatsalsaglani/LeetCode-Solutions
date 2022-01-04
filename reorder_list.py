"""
leetcode: https://leetcode.com/problems/reorder-list/
"""

from collections import deque

def reorderList(head):

    if not head:
        return
    
    q = deque()
    node = head
    while node.next:
        node = node.next
        q.append(node)
    
    while q:
        if head:
            temp = q.pop()
            head.next = temp
            head = head.next
        if head and q:
            temp = q.popleft()
            head.next = temp
            head = head.next
    
    head.next = None