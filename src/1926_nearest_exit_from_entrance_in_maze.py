from typing import *
from collections import *

from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        R = len(maze)
        C = len(maze[0])

        def neighbours(r, c):
            for rows, cols in ((r - 1, c),
                               (r + 1, c),
                               (r, c - 1),
                               (r, c + 1)):
                if 0 <= rows < R and 0 <= cols < C:
                    yield rows, cols

        si, sj = entrance
        start = (si, sj, 0)

        q = deque()
        q.append(start)

        # to the find the shortest path to the exit
        # exit is an empty cell in the border of the maze

        # So to search the border for an empty cell

        exits = []

        for i, rows in enumerate(maze):
            for j, cols in enumerate(rows):
                if maze[i][j] == '.' and (i, j) != (si, sj):
                    if i == 0 or i == R - 1:
                        exits.append((i, j))
                    elif j == 0 or j == C - 1:
                        exits.append((i, j))
        print(f"The exits are: {exits}")

        visited = set()
        visited.add(start)

        while q:
            print("The queue is:", q)
            node = q.popleft()
            x, y, dist = node
            if (x, y) in exits:
                return dist

            for nei in neighbours(x, y):
                nx, ny = nei
                if maze[nx][ny] == '.' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, dist + 1))
        return -1

if __name__ == '__main__':
    maze = [[".","+"]]
    entrance = [0,0]
    s = Solution()
    res = s.nearestExit(maze, entrance)
    print("The result is:", res)