"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


def reverse(num):
    return num[::-1]


if __name__ == "__main__":
    num = "321"
    op = reverse(num)
    print(op)
