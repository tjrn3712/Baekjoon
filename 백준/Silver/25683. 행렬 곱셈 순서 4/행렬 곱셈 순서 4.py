import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
ans = 0
mat = []
for i in range(n):
    r,c = minput()
    mat.append((r,c))
for i in range(n-2,-1,-1):
    ans += mat[i][0]*mat[i][1]*mat[-1][1]
print(ans)

