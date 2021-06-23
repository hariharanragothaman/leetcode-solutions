"""
Given a string s, find the length of the longest substring without repeating characters

I/P: s = "abcabcbb" 
O/P: 3 
answer is: "abc" - with the length of 3

I/P: s = "bbbbb"
O/P: 1
answer is "b" - with the length of 1
"""


def longest_substring_without_repeating_chars(string: str) -> int:
    max_length = 0
    left, right = 0, 0
    seen = {}

    for i, char in enumerate(string):
        if char not in seen or seen[char] < left:
            seen[char] = i
            right = i

            if (right - left + 1) > max_length:
                max_length = right - left + 1

        else:
            left = seen[char] + 1
            seen[char] = i

    return max_length


string = "abcabcbb"
output = longest_substring_without_repeating_chars(string)
print("The output is", output)
