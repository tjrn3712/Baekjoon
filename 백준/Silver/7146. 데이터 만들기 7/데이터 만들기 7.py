import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = 71
c = 55
ce = c * (c - 1) // 2
ex = 16
m = ce + ex
print(n, m)
for i in range(c):
    for j in range(i + 1, c):
        print(i, j)
for j in range(c, n):
    print(j - c + 1, j)
