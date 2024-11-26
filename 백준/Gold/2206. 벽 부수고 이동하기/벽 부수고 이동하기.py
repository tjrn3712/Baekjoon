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


n, m = minput()
grid0 = []
grid1 = []
for _ in range(n):
    temp = [*map(int, *[input().rstrip('\n')])]
    grid0.append(temp[:])
    grid1.append(temp[:])
q = deque()
q.append((0, 0, 0))
grid1[0][0], grid0[0][0] = -1, -1
ans = 1
chk = False
while q:
    if grid0[n-1][m-1] or grid1[n-1][m-1]:
        chk = True
        break
    for _ in range(len(q)):
        i, j, k = q.popleft()
        if k:
            if i:
                if grid1[i-1][j] == 0:
                    grid1[i-1][j] = -1
                    q.append((i-1, j, 1))
            if j:
                if grid1[i][j-1] == 0:
                    grid1[i][j-1] = -1
                    q.append((i, j-1, 1))
            if i<n-1:
                if grid1[i+1][j] == 0:
                    grid1[i+1][j] = -1
                    q.append((i+1, j, 1))
            if j<m-1:
                if grid1[i][j+1] == 0:
                    grid1[i][j+1] = -1
                    q.append((i, j+1, 1))
        else:
            if i:
                if grid0[i-1][j] == 0:
                    grid0[i-1][j] = -1
                    grid1[i-1][j] = -1
                    q.append((i-1, j, 0))
                if grid0[i-1][j] == 1:
                    grid0[i-1][j] = -1
                    q.append((i-1, j, 1))
            if j:
                if grid0[i][j-1] == 0:
                    grid0[i][j-1] = -1
                    grid1[i][j-1] = -1
                    q.append((i, j-1, 0))
                if grid0[i][j-1] == 1:
                    grid0[i][j-1] = -1
                    q.append((i, j-1, 1))
            if i<n-1:
                if grid0[i+1][j] == 0:
                    grid0[i+1][j] = -1
                    grid1[i+1][j] = -1
                    q.append((i+1, j, 0))
                if grid0[i+1][j] == 1:
                    grid0[i+1][j] = -1
                    q.append((i+1, j, 1))
            if j<m-1:
                if grid0[i][j+1] == 0:
                    grid0[i][j+1] = -1
                    grid1[i][j+1] = -1
                    q.append((i, j+1, 0))
                if grid0[i][j+1] == 1:
                    grid0[i][j+1] = -1
                    q.append((i, j+1, 1))
    ans += 1
if chk:
    print(ans)
else:
    print(-1)
