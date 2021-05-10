"""
Given a linkedlist, reverse the linkedlist
"""

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        nxt = current.nxt
        current.nxt = prev
        prev = current
        current = nxt
    return prev