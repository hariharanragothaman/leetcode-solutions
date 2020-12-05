"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode:
    def __init__(self):
        self.val = x
        self.next = None

def add_two_numbers(a, b):
    l1 = a
    l2 = b
    carry = 0

    dummy = ListNode(0)
    current = dummy

    while l1 or l2 or carry:

        if l1 is not None:
            value1 = l1
        else:
            value1 = 0

        if l2 is not None:
            value2 = l2
        else:
            value2 = 0

        add = value1 + value2 + carry
        carry = add // 10
        item  = add % 10

        current.next = ListNode(item)
        current = current.next

        if l1:
            l1 = l1.next

        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy.next