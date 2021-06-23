"""
Problem Statement:
Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring text[i]...text[j] is in the list of words.



Example 1:

Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]

Example 2:

Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation:
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].



Note:

    All strings contains only lowercase English letters.
    It's guaranteed that all strings in words are different.
    1 <= text.length <= 100
    1 <= words.length <= 20
    1 <= words[i].length <= 50
    Return the pairs [i,j] in sorted order (i.e. sort them by their first coordinate in case of ties sort them by their second coordinate).

"""


class Trie:
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def __delitem__(self, word):
        current_dict = self.root
        nodes = [current_dict]
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
        del current_dict["_end_"]

    def starts_with(self, prefix):
        current_dict = self.root
        for letter in prefix:
            current = current_dict.get(letter)
            if current is None:
                return False
            current_dict = current_dict[letter]
        return True


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        """
        So the question does not just want the - indexs of where the words are
        But also - all pairs of indices where it's a substring also
        """
        """
        # Non-Trie Solution
        output = []
        for w in words:
            idx = text.find(w)

            while idx != -1:
                output.append([idx, idx+len(w)-1])
                idx = text.find(w, idx+1)

        output.sort()
        return output
        """

        res = []
        # An optimized solution using trie
        t = Trie(*words)
        for left in range(len(text)):
            for right in range(left, len(text)):
                substr = text[left : right + 1]
                if not t.starts_with(substr):
                    break
                if t.__contains__(substr) and substr in words:
                    res.append((left, right))

        res.sort()
        return res
