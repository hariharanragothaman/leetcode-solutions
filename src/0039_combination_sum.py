from typing import List
from collections import deque

"""
The most important things to remember here is that:
1. We are return all the unique combinations
2. The same number from the candidates can be chosen an unlimited number of times

"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        q = deque()
        q.append((target,
                  [],
                  0))
        ans = []

        while q:
            current_target, current_ans, candidate_index = q.popleft()

            for i in range(candidate_index, len(candidates)):
                new_target = current_target - candidates[i]

                if new_target == 0:
                    ans.append(current_ans + [candidates[i]])
                elif new_target > 0:
                    q.append((new_target,
                              current_ans + [candidates[i]],
                              i))
        print(ans)


if __name__ == '__main__':
    s = Solution()
    s.combinationSum(candidates=[2, 3, 6, 7], target=7)