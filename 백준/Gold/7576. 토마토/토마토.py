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
    q = deque(tomato[:])
    while q:
        check = False
        for _ in range(len(q)):
            now = q.popleft()
            i = now[0]
            j = now[1]
            if i>0 and grid[i-1][j] == 0:
                check = True
                grid[i-1][j] = 1
                q.append((i-1, j))
            if i<n-1 and grid[i+1][j] == 0:
                check = True
                grid[i+1][j] = 1
                q.append((i+1, j))
            if j>0 and grid[i][j-1] == 0:
                check = True
                grid[i][j-1] = 1
                q.append((i, j-1))
            if j<m-1 and grid[i][j+1] == 0:
                check = True
                grid[i][j+1] = 1
                q.append((i, j+1))
        if check:
            ans += 1
    return ans



m, n = minput()
grid = []
tomato = []
for i in range(n):
    grid.append(list(minput()))
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            tomato.append((i, j))
ans = bfs(grid)
chk = False
for i in range(n):
    if 0 in grid[i]:
        chk = True
        break
if chk:
    print(-1)
else:
    print(ans)