import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
sol = []
for i in range(n):
    sol.append([*minput()])
sol.sort(key=lambda x: [x[1], -x[0]])
pq = []
for i in range(n):
    heapq.heappush(pq, sol[i][0])
    if len(pq) > sol[i][1]:
        heapq.heappop(pq)
print(sum(pq))