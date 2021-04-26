from typing import List
from collections import defaultdict

"""
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.
"""

class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        g = defaultdict(set)

        for i in range(n):
            for j in range(n):
                if mat[i][j] and i != j:
                    g[i].add(j)
                    g[j].add(i)
        print(g)

        visited = [False] * n
        count = 0

        for i in range(n):
            # Core Logic is: = If it's already visited - then it means it's already connected to something
            if visited[i]:
                continue
            else:
                count += 1

            stack = [i]
            while stack:
                node = stack.pop()
                for nei in g[node]:
                    if not visited[nei]:
                        # If it's a neighbor, you can visit through this node
                        visited[nei] = True
                        stack.append(nei)

        return count

if __name__ == '__main__':
    s = Solution()
    s.findCircleNum(mat=[[1,1,0],[1,1,0],[0,0,1]])