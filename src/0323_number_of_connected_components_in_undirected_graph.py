from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        connected_components = 0

        for i in range(n):
            if visited[i]:
                continue
            else:
                connected_components += 1

            stack = [i]
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

        return connected_components


if __name__ == "__main__":
    s = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    s.countComponents(n, edges)
