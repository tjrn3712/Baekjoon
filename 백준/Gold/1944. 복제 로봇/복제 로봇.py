import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())

def union(a, b):
    a = find(a)
    b = find(b)
    p[a] = p[b]

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def kruskal(edges):
    edges.sort()
    ans = 0
    used = 0
    for cost, a, b in edges:
        ra = find(a)
        rb = find(b)
        if ra != rb:
            union(a, b)
            ans += cost
            used += 1
    return ans, used

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(sx, sy):
    dist2D = [[-1]*N for _ in range(N)]
    dist2D[sx][sy] = 0
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] != '1' and dist2D[nx][ny] == -1:
                    dist2D[nx][ny] = dist2D[x][y] + 1
                    q.append((nx, ny))
    return dist2D

N, M = minput()
maze = [list(input().rstrip()) for _ in range(N)]
points = []
for i in range(N):
    for j in range(N):
        if maze[i][j] == 'S':
            points.append((i, j))
for i in range(N):
    for j in range(N):
        if maze[i][j] == 'K':
            points.append((i, j))
if len(points) < M+1:
    print(-1)
    sys.exit()
dist = [[mod]*(M+1) for _ in range(M+1)]
for i in range(M+1):
    sx, sy = points[i]
    dist2D = bfs(sx, sy)
    for j in range(M+1):
        tx, ty = points[j]
        dist[i][j] = dist2D[tx][ty]
for i in range(M+1):
    for j in range(M+1):
        if dist[i][j] == -1:
            print(-1)
            sys.exit()
edges = []
for i in range(M+1):
    for j in range(i+1, M+1):
        edges.append((dist[i][j], i, j))
p = list(range(M+1))
ans, used = kruskal(edges)
if used < M:
    print(-1)
else:
    print(ans)
