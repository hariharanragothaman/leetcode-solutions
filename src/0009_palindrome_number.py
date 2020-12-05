"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def is_palindrome_without_typecast(number):
    # This condition is defined by the problem statement
    """
     # When num < 0, num is not a palindrome
     # Also if last digit is zero and number is not zero, it's not - since num can only be zero
    """
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    rev_number = 0
    while number > rev_number:  # This while condition indicates it's half completed
        rev_number = rev_number * 10 + number % 10
        number = number // 10

    # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
    # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
    # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.>
    return number == rev_number or (number == rev_number // 10)


if __name__ == '__main__':
    value = 121
    op = is_palindrome(value)
    print(op)
    op2 = is_palindrome_without_typecast(value)
    print(op2)
