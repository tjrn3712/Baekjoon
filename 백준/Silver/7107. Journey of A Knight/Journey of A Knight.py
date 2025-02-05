import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n, m, tr, tc = minput()
moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
q = deque([(1, 1, 0)])
visited = [[False]*(m+1) for _ in range(n+1)]
visited[1][1] = True

while q:
    r, c, d = q.popleft()
    if r == tr and c == tc:
        exit(print(d))
    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        if 1 <= nr <= n and 1 <= nc <= m and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr, nc, d+1))

print("NEVAR")
