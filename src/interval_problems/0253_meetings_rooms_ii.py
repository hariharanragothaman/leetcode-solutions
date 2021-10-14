"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Input: [[7,10],[2,4]]
Output: 1

This was a very interesting question; but if we think about chronologically we can get it.
Assume a meeting is already happening.
So obviously for that meeting - start_time will be less than end_time right?
we increment the number of rooms
Now - we go to the next meeting - If start_time for this meeting is less than end_time of the previous meeting
- Obviously we need a room. Since these meetings have to happen in parallel.
When the start time is greater than the end-time, then, it means, the previous meeting has ended :slight_smile:
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0

        start_time = sorted(c[0] for c in intervals)
        end_time = sorted(c[1] for c in intervals)

        print(start_time)
        print(end_time)

        e = 0

        for i in range(len(start_time)):
            if start_time[i] < end_time[e]:
                rooms += 1
            else:
                e += 1
        return rooms


if __name__ == "__main__":
    s = Solution()
    arr = [[0, 30], [5, 10], [15, 20]]
    res = s.minMeetingRooms(arr)
    print("The minimum rooms required is:", res)
