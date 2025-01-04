import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n, m = minput()
arr = [*minput()]
d = dict()
for i in range(n):
    d[arr[i]] = i
arr.sort()
dd = []
for i in range(n):
    dd.append(d[arr[i]])
for _ in range(m):
    i, j, k = minput()
    i-=1
    j-=1
    cnt = 0
    ind = 0
    while True:
        if i <= dd[ind] <= j:
            cnt += 1
        if cnt == k:
            print(arr[ind])
            break
        ind += 1