from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for q in queries:
            x, y, r = q
            cnt = 0
            for p in points:
                xp, yp = p
                if (xp-x)**2 + (yp-y)**2 <= r**2:
                    cnt += 1
            result.append(cnt)
        print(*result)
        return result



if __name__ == '__main__':
    s = Solution()
    points, queries = [[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]]
    s.countPoints(points, queries)