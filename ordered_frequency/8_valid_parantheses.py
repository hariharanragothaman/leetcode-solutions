"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""

def check_valid_parantheses(string):
    opened = ["(", "{", '[']
    closed = [")", "}", "]"]

    stack = []

    for i in range(len(string)):
        if string[i] in opened:
            stack.append(string[i])
        elif string[i] in closed:
            index = closed.index(string[i])
            if stack and stack[-1] == opened[index]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True