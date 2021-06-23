from typing import List

"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.


Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true


"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # To determine if a person can attend all meetings
        intervals = sorted(intervals)
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    res = s.canAttendMeetings(intervals=[[0, 30], [5, 10], [15, 20]])
    print("The result is:", res)
