from typing import List


class Trie:
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        if self.__contains__(word):
            for letter in word:
                current_dict = current_dict[letter]
            current_dict["_cnt_"] += 1
            return

        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True
        current_dict["_cnt_"] = 1

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


class Solution:
    def search_trie(board, trie, result, rows, cols, path=None, node=None, word=None):

        letter = board[rows][cols]

        if node is None or path is None or word is None:
            pass

    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        result = set()
        words = [word]
        print(words)
        trie_obj = Trie(*words)
        print(trie_obj.root)


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    s = Solution()
    print(s.exist(board, word))
