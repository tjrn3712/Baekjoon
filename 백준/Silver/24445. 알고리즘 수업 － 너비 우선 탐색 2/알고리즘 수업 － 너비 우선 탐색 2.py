import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def bfs(graph, i, visited):
    q = deque()
    t = 1
    if not visited[i]:
        visited[i] = True
        nums[i] = t
        t += 1
        for j in sorted(graph[i], reverse=True):
            q.append(j)
    while q:
        temp = q.popleft()
        if not visited[temp]:
            nums[temp] = t
            t += 1
            visited[temp] = True
            for j in sorted(graph[temp], reverse=True):
                q.append(j)


n, m, r = minput()
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = minput()
    graph[u].append(v)
    graph[v].append(u)
nums = [0]*(n+1)
bfs(graph, r, visited)

for i in range(1, n+1):
    print(nums[i])
