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
            i, j, k = q.popleft()
            if i>0 and grid[k][i-1][j] == 0:
                check = True
                grid[k][i-1][j] = 1
                q.append((i-1, j, k))
            if i<n-1 and grid[k][i+1][j] == 0:
                check = True
                grid[k][i+1][j] = 1
                q.append((i+1, j, k))
            if j>0 and grid[k][i][j-1] == 0:
                check = True
                grid[k][i][j-1] = 1
                q.append((i, j-1, k))
            if j<m-1 and grid[k][i][j+1] == 0:
                check = True
                grid[k][i][j+1] = 1
                q.append((i, j+1, k))
            if k>0 and grid[k-1][i][j] == 0:
                check = True
                grid[k-1][i][j] = 1
                q.append((i, j, k-1))
            if k<h-1 and grid[k+1][i][j] == 0:
                check = True
                grid[k+1][i][j] = 1
                q.append((i, j, k+1))
        if check:
            ans += 1
    return ans



m, n, h = minput()
grid = [[] for k in range(h)]
for k in range(h):
    for i in range(n):
        grid[k].append(list(minput()))
tomato = [(i, j, k) for k in range(h) for i in range(n) for j in range(m) if grid[k][i][j] == 1]
ans = bfs(grid)
chk = False
for i in range(h):
    for j in range(n):
        if 0 in grid[i][j]:
            chk = True
            break
if chk:
    print(-1)
else:
    print(ans)