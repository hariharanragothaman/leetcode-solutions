"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:

Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].

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
    def longestWord(self, words: List[str]) -> str:
        t = Trie(*words)
        print(t.root)
        # Approach 1 - Trie + Sorting
        hmap = {}
        words = sorted(words, reverse=True)
        for w in words:
            check_flag = True
            for i in range(len(w)):
                candidate = w[:i + 1]
                if not t.__contains__(candidate):
                    check_flag = False
                    break
            if check_flag:
                hmap[w] = len(w)

        max_length = max(hmap.values())
        hmap = {k: v for k, v in hmap.items() if v == max_length}
        return sorted(hmap.keys())[0]

        # Approach2: Now, we need to see how we can parse the trie to search for the longest word
        # This is classic DFS into the hashmap - NICE!
