from collections import defaultdict
from typing import List


class Solution:
    def allPathsSourceTarget(self, edges: List[List[int]]) -> List[List[int]]:
        all_paths = []
        graph = defaultdict(list)

        for i, e in enumerate(edges):
            for d in e:
                graph[i].append(d)

        number_of_nodes = len(edges)
        start, end = 0, number_of_nodes - 1

        # using all paths recipe

        def find_all_paths(start, end, path=[]):
            all_paths = []

            # This line is creating each path, and start changes during every recursion call
            path = path + [start]

            print(f"The all paths are {all_paths}")
            print("The path is: ", path)

            # When you reachthe end of one full-path, that is returned
            if start == end:
                return [path]

            if start not in graph:
                return None

            for node in graph[start]:
                print("The node is ", node)
                if node not in path:
                    new_paths = find_all_paths(node, end, path)
                    print(f"The new paths is {new_paths}")

                    for np in new_paths:
                        all_paths.append(np)

            return all_paths

        result = find_all_paths(start, end)
        return result
