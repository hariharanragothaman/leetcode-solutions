"""
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.



Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.

Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.



Constraints:

    1 <= str1.length == str2.length <= 104
    str1 and str2 contain only lowercase English letters.


"""

"""
Solution Explanation:

aa b cc
cc d ee 

From a graphical standpoint, this is how things are getting converted

a -> c 
b -> d
c -> e

So, if there is a cycle - Then one can't really convert one string to another
This is the graphical view point behind this.

So we can use a hashmap to store the mapping
and obviously if one character cannot be mapped to multiple characters
So, if that happens - we can instantly return False

On the other hand - now we come to another corner case?
So - we have 26 characters, if all the 26 characters are used -- ?
Then  - it means, there is definitely a cycle?

We can use the check_cycle_in_a_graph template to figure that out?
or a smarter way to check is to see if set(s2) < 26
as in there is atleast one character, that has not been mapped

"""


def can_convert(s1, s2):
    # Given I/P both are same strings
    if s1 == s2:
        return True

    hashmap = {}
    for i, j in zip(s1, s2):
        if hashmap.setdefault(i, j) != j:
            return False
    return len(set(s2)) < 26
