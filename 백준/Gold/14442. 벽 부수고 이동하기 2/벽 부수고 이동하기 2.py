import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
INF = float('inf')
MOD = 998244353
def minput(): return map(int, input().split())


n, m, limit = minput()
grid = []
for _ in range(n):
    temp = [*map(int, *[input().rstrip('\n')])]
    grid.append(temp[:])
grid = [grid]
for _ in range(limit):
    grid.append([[grid[0][i][j] for j in range(m)] for i in range(n)])
q = deque()
q.append((0, 0, 0))
for i in range(limit+1):
    grid[i][0][0] = -1
ans = 1
chk = False
i=j=0
while q:
    for qwer in range(limit+1):
        if grid[qwer][n-1][m-1]:
            chk = True
            break
    if chk:
        break
    for _ in range(len(q)):
        i, j, k = q.popleft()
        if k == limit:
            if i:
                if grid[k][i-1][j] == 0:
                    grid[k][i-1][j] = -1
                    q.append((i-1, j, k))
            if j:
                if grid[k][i][j-1] == 0:
                    grid[k][i][j-1] = -1
                    q.append((i, j-1, k))
            if i<n-1:
                if grid[k][i+1][j] == 0:
                    grid[k][i+1][j] = -1
                    q.append((i+1, j, k))
            if j<m-1:
                if grid[k][i][j+1] == 0:
                    grid[k][i][j+1] = -1
                    q.append((i, j+1, k))
        else:
            if i:
                if grid[k][i-1][j] == 0:
                    for asdf in range(k, limit+1):
                        grid[asdf][i-1][j] = -1
                    q.append((i-1, j, k))
                if grid[k][i-1][j] == 1:
                    for asdf in range(k, limit+1):
                        grid[asdf][i-1][j] = -1
                    q.append((i-1, j, k+1))
            if j:
                if grid[k][i][j-1] == 0:
                    for asdf in range(k, limit+1):
                        grid[asdf][i][j-1] = -1
                    q.append((i, j-1, k))
                if grid[k][i][j-1] == 1:
                    for asdf in range(k, limit+1):
                        grid[asdf][i][j-1] = -1
                    q.append((i, j-1, k+1))
            if i<n-1:
                if grid[k][i+1][j] == 0:
                    for asdf in range(k, limit+1):
                        grid[asdf][i+1][j] = -1
                    q.append((i+1, j, k))
                if grid[k][i+1][j] == 1:
                    for asdf in range(k, limit+1):
                        grid[asdf][i+1][j] = -1
                    q.append((i+1, j, k+1))
            if j<m-1:
                if grid[k][i][j+1] == 0:
                    for asdf in range(k, limit+1):
                        grid[asdf][i][j+1] = -1
                    q.append((i, j+1, k))
                if grid[k][i][j+1] == 1:
                    for asdf in range(k, limit+1):
                        grid[asdf][i][j+1] = -1
                    q.append((i, j+1, k+1))
    ans += 1
if chk:
    print(ans)
else:
    print(-1)
