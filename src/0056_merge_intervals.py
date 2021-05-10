"""
Given a collection of intervals, merge all overlapping intervals

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        merged = []
        n = len(intervals)

        for i in range(n):
            cstart, cend = intervals[i]
            if not merged or cstart > merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])

        return merged

if __name__ == '__main__':
    intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    s = Solution()
    res = s.merge(intervals)
    print("The merged intervals are:", res)