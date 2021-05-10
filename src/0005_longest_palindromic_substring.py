"""
Given a string s, find the longest palindromic substring in it.
I/P : "babad"
O/P : "bab"
"aba" is also a valid answer

I/P: "cbbd"
O/P: "bb
"""
# Approach 0 - get all possible substrings and check for palindrome.
# Approach 1: Using sliding window - Expanding around the center
"""
The core logic in this is:
1. Keep one-pointer from the start of the string
2. Keep second-pointer from the end of the string
3. Because you are starting from reverse
"""


def longest_palindromic_substring(string):
    result = []
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            if len(result) > j-i: # This means we have found it.
                break
            elif string[i:j] == string[i:j][::-1]:
                result = string[i:j]
                break
    return result