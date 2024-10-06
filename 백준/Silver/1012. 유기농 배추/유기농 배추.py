import sys
from collections import deque
import math
ipt = sys.stdin.readline
sys.setrecursionlimit(10**9)
def minput(): return map(int, ipt().split())
def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if grid[x][y] == 1:
        grid[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


t = int(ipt())
for i in range(t):
    cnt = 0
    m, n, k = minput()
    grid = [[0] * n for ii in range(m)]
    for iii in range(k):
        x, y = minput()
        grid[x][y] = 1

    for iv in range(n):
        for v in range(m):
            if dfs(v, iv):
                cnt += 1

    print(cnt)


