import sys
input = sys.stdin.readline
from collections import deque
def minput(): return map(int, input().split())


n, m = minput()
d = [(1,0),(-1,0),(0,1),(0,-1)]
grid = []
for _ in range(n):
    grid.append([*minput()])
grid[0][0] = 'O'
cnt = 0
while True:
    chk = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                chk = True
    if not chk: break
    visited = [[False]*m for _ in range(n)]
    cnt += 1
    nxt = []
    for _ in range(n):
        nxt.append(grid[_][:])
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni, nj = i+di,j+dj
            if 0<=ni<n and 0<=nj<m:
                if grid[i][j] == 0 or grid[i][j] == 'O':
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        q.append((ni, nj))
                    if grid[ni][nj] == 0 or grid[ni][nj] == 'O':
                        grid[ni][nj] = 'O'
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                temp = 0
                for di, dj in d:
                    ni, nj = i+di, j+dj
                    if 0<=ni<n and 0<=nj<m:
                        if not visited[ni][nj]:
                            visited[ni][nj] = True
                            q.append((ni, nj))
                        if grid[ni][nj] == 'O':
                            temp += 1
                if grid[i][j] == 1 and temp >= 2:
                    nxt[i][j] = 'O'
    for _ in range(n):
        grid[_] = nxt[_][:]

print(cnt)
