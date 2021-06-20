from collections import defaultdict
from bisect import bisect_left


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_structure = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data_structure[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """bisect_left approach - is somehow weirdly TLE'ing """
        """
        if key in self.data_structure:
            _tmp = self.data_structure[key]
            times = [c[0] for c in _tmp]

            index = bisect_left(times, timestamp)
            if index != len(times) and times[index] == timestamp:
                return _tmp[index][1]
            else:
                if index - 1 >= 0:
                    return _tmp[index - 1][1]
                else:
                    return ""
        else:
            return ""
        """
        if key in self.data_structure:
            arr = self.data_structure[key]

            n = len(arr)
            left, right = 0, n

            while left < right:
                mid = (left + right) >> 1
                if arr[mid][0] <= timestamp:
                    left = mid + 1
                elif arr[mid][0] > timestamp:
                    right = mid

            return "" if right == 0 else arr[right - 1][1]


if __name__ == "__main__":
    obj = TimeMap()

    obj.set("love", "high", 10)
    obj.set("love", "low", 20)

    res = obj.get("love", 5)
    print(f"The result is: {res}")
    print("*" * 10)

    res = obj.get("love", 10)
    print(f"The result is: {res}")
    print("*" * 10)

    res = obj.get("love", 15)
    print(f"The result is: {res}")
    print("*" * 10)

    res = obj.get("love", 20)
    print(f"The result is: {res}")
    print("*" * 10)

    res = obj.get("love", 25)
    print(f"The result is: {res}")
    print("*" * 10)

    # obj.set("foo", "bar2", 4)
    #
    # res = obj.get("foo", 4)
    # print(f"The result is: {res}")
    # print("*"*10)
    #
    # res = obj.get("foo", 5)
    # print(f"The result is: {res}")
    # print("*"*10)
