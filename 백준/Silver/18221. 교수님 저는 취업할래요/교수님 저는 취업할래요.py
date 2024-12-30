import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
INF = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
grid = []
for _ in range(n):
    grid.append([*minput()])


for y in range(n):
    for x in range(n):
        if grid[x][y] == 2:
            s = (x, y)
        elif grid[x][y] == 5:
            p = (x, y)
cnt = 0
for y in range(min(p[1], s[1]), max(p[1], s[1])+1):
    for x in range(min(p[0], s[0]), max(p[0], s[0])+1):
        if grid[x][y] == 1:
            cnt += 1
if cnt >= 3 and (s[0]-p[0])**2 + (s[1]-p[1])**2 >= 25:
    print(1)
else:
    print(0)