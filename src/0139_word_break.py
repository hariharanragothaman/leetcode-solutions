from typing import *
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Apply classic DFS
        q = deque([s])
        visited = set()

        while q:
            node = q.popleft()
            for word in wordDict:
                if node.startswith(word):
                    new_node = node[len(word) :]
                    if new_node == "":
                        return True

                    if new_node not in visited:
                        visited.add(new_node)
                        q.append(new_node)
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.wordBreak()
    print(f"The result is: {result}")
