from collections import defaultdict


class Solution:
    def reorderLogFiles(self, logs):
        # Letter logs - identifier + <string of words>
        # Digit Logs -  identifier + <numbers>
        """
        Reorder them in such a way that:
        1. letter logs come before digit logs
        2. letter logs are lexicographically sorted
            If their contents are the same, then sort them lexicographically by their identifiers.
        3. digits logs maintain their relative ordering
        :param logs:
        :return:
        """
        def f(log):
            _id, rest = log.split(" ", 1)
            return (0, rest, _id) if rest[0].isalpha() else(1, )

        return sorted(logs, key=f)



if __name__ == '__main__':
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    logs2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    s = Solution()
    ans = s.reorderLogFiles(logs)
    print(ans)