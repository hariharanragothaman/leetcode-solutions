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
            if len(result) > j - i:  # This means we have found it.
                break
            elif string[i:j] == string[i:j][::-1]:
                result = string[i:j]
                break
    return result


def longest_palindromic_substring_bruteforce(string):
    best = ""
    for left in range(len(string)):
        for right in range(left, len(string)):
            substring = s[left : right + 1]
            if substring == substring[::-1] and len(substring) > len(best):
                best = substring
    return best


# remember if there is more than one odd - the palindrome cannot be formed.
# This solution is through DP O(n^2)


def longest_palindromic_substring_expand_center(string):
    pass


if __name__ == "__main__":
    s = ""
    result = longest_palindromic_substring_expand_center(s)
    print(result)
