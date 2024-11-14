import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def bfs(grid):
    ans = 0
    while q:
        ans += 1
        for ii in range(len(q)):
            i, j = q.popleft()
            if i>0 and grid[i-1][j] and not visited[i-1][j]:
                visited[i - 1][j] = True
                grid[i-1][j] = ans
                q.append((i-1, j))
            if i<n-1 and grid[i+1][j] and not visited[i+1][j]:
                visited[i + 1][j] = True
                grid[i+1][j] = ans
                q.append((i+1, j))
            if j>0 and grid[i][j-1] and not visited[i][j-1]:
                visited[i][j-1] = True
                grid[i][j-1] = ans
                q.append((i, j-1))
            if j<m-1 and grid[i][j+1] and not visited[i][j+1]:
                visited[i][j + 1] = True
                grid[i][j+1] = ans
                q.append((i, j+1))


n, m = minput()
grid = [[] for i in range(n)]
visited = [[False for j in range(m)] for i in range(n)]
q = deque()
for _ in range(n):
    grid[_] = list(minput())
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            grid[i][j] = 0
            visited[i][j] = True
            q.append((i, j))
        if grid[i][j] == 0:
            visited[i][j] = True
bfs(grid)
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            grid[i][j] = -1
        print(grid[i][j], end=' ')
    print()
