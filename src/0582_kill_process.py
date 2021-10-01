from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.g = defaultdict(list)

    def killProcess(self, pid, ppid, kill):
        for process, parent in zip(pid, ppid):
            self.g[parent].append(process)

        q = deque()
        q.append(kill)
        result = set()
        result.add(kill)
        while q:
            node = q.popleft()
            for child in self.g[node]:
                result.add(child)
                q.append(child)
        return list(result)


if __name__ == '__main__':
    s = Solution()
    pid = [1,3,10,5]
    ppid = [3,0,5,3]
    kill = 5
    s.killProcess(pid, ppid, kill)