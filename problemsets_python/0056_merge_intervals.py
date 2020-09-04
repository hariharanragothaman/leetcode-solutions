"""
Given a collection of intervals, merge all overlapping intervals

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def merge_intervals(intervals):
    intervals.sort()
    result = []

    for i in range(len(intervals)):
        if not result or intervals[i][0] > result[-1][1]:
            result.append(intervals)
        else:
            result[-1][1] = max(intervals[i][1], result[-1][1])
    return result