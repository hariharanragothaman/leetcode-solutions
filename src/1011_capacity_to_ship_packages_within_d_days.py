from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def condition(capacity) -> bool:
            days = 1
            total = 0

            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    days += 1
                    if days > D:
                        return False
                print("The total is:", total)
            print("The number of days is:", days)
            return True

        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            print("The mid value is:", mid)
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
