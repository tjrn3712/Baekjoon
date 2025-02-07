import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
a = []
for i in range(n):
    a.append([*minput()])
a.sort()
ps = [0]*n
temp = 0
mx = a[0][0]
mn = a[0][0]
for i in range(n):
    temp += a[i][1]
    ps[i] = temp
ans = 0
for i in range(n):
    mx = a[i][0]
    temp = ps[i] - mx + mn
    ans = max(ans, temp)
    if i != n-1:
        mn = max(mn, a[i+1][0]-ps[i])
print(ans)