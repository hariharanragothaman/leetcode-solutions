"""

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:

Input: sentence = "leetcode"
Output: false



Constraints:

    1 <= sentence.length <= 1000
    sentence consists of lowercase English letters.



"""

from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = [chr(c) for c in range(ord("a"), ord("z") + 1)]
        print(alpha)

        ctr = Counter(sentence)
        keys = sorted(ctr.keys())

        if alpha == keys:
            return True
        return False
