import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def bfs(i, j):
    global ans
    now = grid[i][j]
    q = deque([(i, j)])
    while q:
        i, j = q.popleft()
        if i>0 and grid[i-1][j] == now and not visited[i-1][j]:
            visited[i-1][j] = True
            q.append((i-1, j))
        if i<n-1 and grid[i+1][j] == now and not visited[i+1][j]:
            visited[i+1][j] = True
            q.append((i+1, j))
        if j>0 and grid[i][j-1] == now and not visited[i][j-1]:
            visited[i][j-1] = True
            q.append((i, j-1))
        if j<n-1 and grid[i][j+1] == now and not visited[i][j+1]:
            visited[i][j+1] = True
            q.append((i, j+1))
    ans += 1

n = int(ipt())
grid = []
visited = [[False for i in range(n)] for j in range(n)]
for _ in range(n):
    grid.append(ipt().rstrip('\n'))
ans = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
ans1 = ans
visited = [[False for i in range(n)] for j in range(n)]
ans = 0
for i in range(n):
    grid[i] = grid[i].replace('G', 'R')
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
ans2 = ans
print(ans1, ans2)
