from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        print(intervals)
        n = len(intervals)
        cnt = 1

        m = [item for sublist in intervals for item in sublist]
        ROOMS = [0] * (max(m) + 1)
        ROOMS[intervals[0][1]] = 1

        for i in range(1, n):

            alloc_flag = False
            cstart, cend = intervals[i]

            # Mark the time, when a room can become available
            ROOMS[cend] += 1

            # Check if empty rooms are available - before allocating a room
            for j in range(cstart + 1):
                if ROOMS[j]:
                    ROOMS[j] -= 1
                    alloc_flag = True
                    break

            # if the previous hasn't been completed:
            if not alloc_flag and intervals[i][0] < intervals[i - 1][1]:
                cnt += 1

        return cnt
