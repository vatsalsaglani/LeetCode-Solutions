"""
leetcode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def removeNthNodeFromEnd(head, n):

    # add a dummy node at starting of the list
    # left pointer at dummy node
    # right pointer at head node
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # move right pointer till n is not equal to 0
    while n > 0 and right:
        right = right.next
        n -= 1
    
    # while right is not at end move left and right
    while right:
        left = left.next
        right = right.next
    
    # left will be at n-1 node.
    # change referece of left to reference of n.next
    left.next = left.next.next

    return dummy.next
