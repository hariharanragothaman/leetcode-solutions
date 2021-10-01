import itertools

class Solution:
    def compareVersion(self, version1, version2):
        version1 = version1.split('.')
        version2 = version2.split('.')

        for c in itertools.zip_longest(version1, version2, fillvalue="0"):
            print(c)
            if int(c[1]) > int(c[0]):
                return -1
            elif int(c[1]) < int(c[0]):
                return 1
        return 0




if __name__ == '__main__':
    s = Solution()
    v1, v2 = "7.5.2.4", "7.5.3"
    op = s.compareVersion(v1, v2)
    print(f"The result is: {op}")