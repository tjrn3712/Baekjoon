import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def bfs(graph, i, visited):
    ans = 1
    q = deque()
    if not visited[i]:
        visited[i] = True
        for j in sorted(graph[i], reverse=True):
            q.append(j)
    else:
        return
    while q:
        temp = q.popleft()
        if not visited[temp]:
            ans += 1
            visited[temp] = True
            for j in sorted(graph[temp], reverse=True):
                q.append(j)
    answer.append(ans)


n = int(ipt())
grid = []
for _ in range(n):
    grid.append(list(map(int, list(ipt().rstrip('\n')))))
graph = [[] for i in range(pow(n,2)+1)]
danzi = [False] * (pow(n,2)+1)
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            danzi[i*n+j+1] = True
            if i>0 and grid[i-1][j]:
                graph[i * n + j + 1].append((i - 1) * n + j + 1)
                graph[(i - 1) * n + j + 1].append(i * n + j + 1)
            if i<n-1 and grid[i+1][j]:
                graph[i * n + j + 1].append((i + 1) * n + j + 1)
                graph[(i + 1) * n + j + 1].append(i * n + j + 1)
            if j>0 and grid[i][j-1]:
                graph[i * n + j + 1].append(i * n + j)
                graph[i * n + j].append(i * n + j + 1)
            if j<n-1 and grid[i][j+1]:
                graph[i * n + j + 1].append(i * n + j + 2)
                graph[i * n + j + 2].append(i * n + j + 1)
visited = [False] * (pow(n,2)+1)
an = 0
answer = []
for i in range(1, pow(n,2)+1):
    if danzi[i]:
        bfs(graph, i, visited)
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])
