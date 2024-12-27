import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10**9)
mod = 998244353
def minput(): return map(int, input().split())

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    p[a] = p[b]

n, m = minput()
p = [i for i in range(n+1)]
for _ in range(m):
    line = [*minput()]
    if line[0]:
        if find(line[1]) == find(line[2]):
            print('YES')
        else:
            print('NO')
    else:
        union(line[1], line[2])
