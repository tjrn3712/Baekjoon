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
        i, j = q.popleft()
        if i>0 and grid[i-1][j] == 'P':
            ans += 1
            grid[i-1][j] = 'I'
            q.append((i-1, j))
        if i>0 and grid[i-1][j] == 'O':
            grid[i-1][j] = 'I'
            q.append((i-1, j))
        if i<n-1 and grid[i+1][j] == 'P':
            ans += 1
            grid[i+1][j] = 'I'
            q.append((i+1, j))
        if i<n-1 and grid[i+1][j] == 'O':
            grid[i+1][j] = 'I'
            q.append((i+1, j))
        if j>0 and grid[i][j-1] == 'P':
            ans += 1
            grid[i][j-1] = 'I'
            q.append((i, j-1))
        if j>0 and grid[i][j-1] == 'O':
            grid[i][j-1] = 'I'
            q.append((i, j-1))
        if j<m-1 and grid[i][j+1] == 'P':
            ans += 1
            grid[i][j+1] = 'I'
            q.append((i, j+1))
        if j<m-1 and grid[i][j+1] == 'O':
            grid[i][j+1] = 'I'
            q.append((i, j+1))
    return(ans)


n, m = minput()
grid = [[] for i in range(n)]
q = deque()
for _ in range(n):
    grid[_] = list(ipt().rstrip('\n'))
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'I':
            q.append((i, j))
            break
ans = bfs(grid)
if ans:
    print(ans)
else:
    print('TT')
