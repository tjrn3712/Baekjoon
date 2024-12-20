import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
INF = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


t = int(input())
for _ in range(t):
    n = int(input())
    inp = [*minput()]
    woods = []
    visited = [False]*n
    for i in range(0, 2*n, 2):
        woods.append([inp[i], inp[i+1]])
    woods.sort()
    temp = -1
    cnt = -1
    f = True
    while f:
        f = False
        for j in range(n):
            if woods[j][1] >= temp and not visited[j]:
                temp = woods[j][1]
                visited[j] = True
                f = True
        temp = -1
        cnt += 1

    print(cnt)


