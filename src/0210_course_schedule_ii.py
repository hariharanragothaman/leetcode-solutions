"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # So this a directed graph
        g = {}
        for i in range(numCourses): g[i] = []

        for u, v in prerequisites:
            g[v].append(u)
        # print(g)

        # Applying topological sort
        in_degree = [0] * numCourses
        idx = [0] * numCourses

        # Counting the indegree
        for i in range(numCourses):
            for edge in g[i]:
                in_degree[edge] += 1

        q = []
        topo_sort = []

        # Adding all elements with indegree zero into the queue
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)


        nr = 0

        while q:
            node = q.pop()
            topo_sort.append(node)

            idx[topo_sort[-1]], nr = nr, nr + 1

            for edge in g[topo_sort[-1]]:
                in_degree[edge] -= 1
                if in_degree[edge] == 0:
                    q.append(edge)

        if numCourses == nr:
            return topo_sort
        else:
            return []